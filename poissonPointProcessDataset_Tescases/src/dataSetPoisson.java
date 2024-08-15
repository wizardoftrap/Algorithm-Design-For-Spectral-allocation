import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Objects;
import java.util.Random;

import javax.swing.JFrame;
import javax.swing.SwingUtilities;
import javax.swing.WindowConstants;

public class dataSetPoisson {

	static class Coordinate {
		private final double x;
		private final double y;

		public Coordinate(double x, double y) {
			this.x = x;
			this.y = y;
		}

		public double getX() {
			return x;
		}

		public double getY() {
			return y;
		}
	}

	static int countPoints = 0;

	public static void main(String[] args) {
		double minX = 0;
		double minY = 0;
		double maxX = 1000;
		double maxY = 1000;
		double rate = 	80; // sparse and dense

		//creating channels
		Map<Integer, Integer> channels = new HashMap();
		
		int numberOfChannels = 30;
		Random random = new Random();
		for (int i = 1; i <= numberOfChannels; i++) {
			int frequency = 81000; //Hz
			channels.put(i, frequency + i * 1000);
		}
		
        //generating coordinates and no of coordinates(poisson process)
		List<dataSetPoisson.Coordinate> generatedPoints = generateCoordinates(minX, minY, maxX, maxY, rate);
		//generating frequencies
		ArrayList<Integer> frequencies = generateRandomFrequencies(countPoints, channels);
		//generating ranges
		List<Double> ranges = generateRandomRanges(countPoints, 0, 1);
		System.out.println(countPoints);
		//dataset in csv format
		writeDataToFileCSV(generatedPoints, frequencies, ranges, "new_sparse.csv", channels);
		//dataset in txt format
		writeDataToFileTXT(generatedPoints, frequencies, ranges, "new_sparse.txt", channels);

		// point plot
		// plotPoints(generatedPoints);
		//circle plot
		SwingUtilities.invokeLater(() -> {
			JFrame frame = new JFrame("Circle Plotter");
			frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
			frame.setSize(5000, 5000);
			circlePlotter circlePlotter = new circlePlotter(generatedPoints, ranges);
			frame.add(circlePlotter);
			frame.setLocationRelativeTo(null);
			frame.setVisible(true);
			frame.setVisible(true);
		});
	}

	public static List<dataSetPoisson.Coordinate> generateCoordinates(double minX, double minY, double maxX,
			double maxY, double rate) {
		List<Coordinate> coordinates = new ArrayList<>();
		Random random = new Random();
		int noPoissonPoints = getPoissonRandom(rate);

		for (int j = 0; j < noPoissonPoints; j++) {
			double x = minX + random.nextDouble() * (maxX - minX);
			double y = minY + random.nextDouble() * (maxY - minY);
			coordinates.add(new Coordinate(Math.round(x * 100.0) / 100.0, Math.round(y * 100.0) / 100.0));
			countPoints++;
		}

		return coordinates;
	}

	private static int getPoissonRandom(double rate) {
		double L = Math.exp(-rate);
		double p = 1.0;
		int k = 0;

		do {
			k++;
			p *= Math.random();
		} while (p > L);

		return k - 1;
	}

	public static <T, E> T getKeyByValue(Map<T, E> map, E value) {
		for (Entry<T, E> entry : map.entrySet()) {
			if (Objects.equals(value, entry.getValue())) {
				return entry.getKey();
			}
		}
		return null;
	}

	public static ArrayList<Integer> generateRandomFrequencies(int numPoints, Map channels) {
		ArrayList<Integer> frequencies = new ArrayList<>();
		Random random = new Random();
		// update dataset

		for (int i = 0; i < countPoints; i++) {
			int channelNo = random.nextInt(30);
			frequencies.add((Integer) channels.get(channelNo + 1));
		}
		// System.out.println(frequencies.size());

		return frequencies;
	}

	public static List<Double> generateRandomRanges(int numPoints, double minRange, double maxRange) {
		List<Double> ranges = new ArrayList<>();
		Random random = new Random();

		for (int i = 0; i < numPoints; i++) {
			ranges.add(minRange + random.nextDouble() * (maxRange - minRange));
		}

		return ranges;
	}

	public static void writeDataToFileCSV(List<dataSetPoisson.Coordinate> generatedPoints, ArrayList<Integer> frequencies,
			List<Double> ranges, String fileName, Map channels) {
		try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName))) {
			// Writing generated points
			writer.write("X,Y,Channel No,Frequency(Hz),Range\n");

			for (int i = 0; i < countPoints; i++) {
				writer.write(generatedPoints.get(i).getX() + "," + generatedPoints.get(i).getY() + ","
						+ getKeyByValue(channels, frequencies.get(i)) + "," + frequencies.get(i) + "," + ranges.get(i)
						+ "\n");
			}

			writer.write("\n");
		}

		catch (

		IOException e) {
			e.printStackTrace();
		}
	}
	public static void writeDataToFileTXT(List<dataSetPoisson.Coordinate> generatedPoints, ArrayList<Integer> frequencies,
			List<Double> ranges, String fileName, Map channels) {
		try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName))) {
			// Writing generated points
			writer.write("X Y Channel No Frequency(Hz) Range\n");

			for (int i = 0; i < countPoints; i++) {
				writer.write(generatedPoints.get(i).getX() + " " + generatedPoints.get(i).getY() + " "
						+ getKeyByValue(channels, frequencies.get(i)) + " " + frequencies.get(i) + " " + ranges.get(i)
						+ "\n");
			}

			writer.write("\n");
		}

		catch (

		IOException e) {
			e.printStackTrace();
		}
	}
}