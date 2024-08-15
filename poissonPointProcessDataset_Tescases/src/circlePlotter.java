import javax.swing.*;
import java.awt.*;
import java.awt.geom.Ellipse2D;
import java.util.*;
import java.util.List;

public class circlePlotter extends JPanel {
	private List<dataSetPoisson.Coordinate> XY;
	private List<Double> radii;
	private int numberOfCircles;

	public circlePlotter(List<dataSetPoisson.Coordinate> generatedPoints, List<Double> ranges) {
		this.XY = generatedPoints;
		this.radii = ranges;
		this.numberOfCircles = generatedPoints.size();
	}

	@Override
	protected void paintComponent(Graphics g) {
		super.paintComponent(g);
		Graphics2D g2d = (Graphics2D) g;
		double xAxisPos = getHeight() / 2;
		double yAxisPos = getWidth() / 2;
		g2d.drawLine(0, getHeight() / 2, getWidth(), getHeight() / 2);
		g2d.drawLine(getWidth() / 2, 0, getWidth() / 2, getHeight());
		for (int i = 0; i < numberOfCircles; i++) {
			double x = XY.get(i).getX() * 4 + yAxisPos;
			double y = xAxisPos - 20 - XY.get(i).getY() * 4;
			double radius = radii.get(i);
			double diameter = 2 * radius;
			g2d.draw(new Ellipse2D.Double(x - radius, getHeight() / 2 - y - radius, diameter, diameter));
		}
	}

}
