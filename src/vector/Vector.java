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
	
	public void scalar(double c)
	{
		x *= c;
		y *= c;
		z *= c;
	}
	
	public Vector add(Vector v2)
	{
		return new Vector(x + v2.x, y + v2.y, z + v2.z, id + "+" + v2.id);
	}
	
	public Vector subtract(Vector v2)
	{
		return new Vector(x - v2.x, y - v2.y, z - v2.z, id + "-" + v2.id);
	}
	
	public double dotProduct(Vector v2)
	{
		return (x * v2.x) + (y * v2.y) + (z * v2.z);
	}
	
	public Vector crossProduct(Vector v2)
	{
		return new Vector( (y * v2.z) - (z * v2.y), (x * v2.z) - (z * v2.x), (x * v2.y) - (y * v2.x), id + "X" + v2.id );    
	}
	
	public boolean isParralel(Vector v2)
	{
		return ( crossProduct(v2) ).equals(new Vector(0, 0, 0, id + "X" + v2.id));
	}
	
	public boolean isOrthoganal(Vector v2)
	{
		return dotProduct(v2) == 0;
	}
	
	public double getAngle(Vector v2)
	{
		return Math.acos( (dotProduct(v2)) / (getMagnitude() * v2.getMagnitude()) );
	}
	
	public double getAngleDegrees(Vector v2)
	{
		return getAngle(v2) * (180/Math.PI);
	}
}
