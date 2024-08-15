import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

public class testCase {

	public static void main(String[] args) {
		double minX = 100;
		double minY = 100;
		double maxX = 900;
		double maxY = 900;
		Random random = new Random();
		
			
			try (BufferedWriter writer = new BufferedWriter(new FileWriter("testCase.csv"))) {
				for (int i = 0; i < 20; i++) {
					double x1 = minX + random.nextDouble() * (maxX - minX);
					double x2=x1+ random.nextDouble() * (10)+10;
					double y1= minX + random.nextDouble() * (maxX - minX);
					double y2=y1+random.nextDouble() * (10)+10;
					double d=random.nextDouble() * (10);
				
				writer.write(x1+","+x2+","+y1+","+y2+","+d);

				writer.write("\n");
			}
			}
			catch (

			IOException e) {
				e.printStackTrace();
			}
		}
	}


