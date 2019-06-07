package thesis.location_manager;

import java.awt.geom.Point2D;

public interface DistanceCalculation {

	public static double distanceCalculation(double x1, double y1, double x2, double y2){
		
		double distance = Point2D.distance(x1, y1, x2, y2);
		
		return distance;
	}
	
}
