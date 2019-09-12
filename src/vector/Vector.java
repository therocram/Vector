package vector;
import java.lang.Math;

public class Vector 
{
	private double x, y, z;
	private String id;
	
	public Vector()
	{
		this(0, 0, 0, "a");
	}
	
	public Vector(double a, double b, double c, String n)
	{
		x = a;
		y = b;
		z = c;
		id = n;
	}
	
	public Vector(Vector v)
	{
		this(v.x, v.y, v.z, v.id);
	}
	
	public double getMagnitude()
	{
		return Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2) + Math.pow(z, 2));
	}
	
	public Vector add(Vector v2)
	{
		return new Vector(x + v2.x, y + v2.y, z + v2.z, id + "+" + v2.id);
	}
	
	public Vector subtract(Vector v2)
	{
		return new Vector(x - v2.x, y - v2.y, z - v2.z, id + "-" + v2.id);
	}
	
	
	
}
