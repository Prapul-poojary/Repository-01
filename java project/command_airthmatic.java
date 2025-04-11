class command_airthmatic
{
	public static void main(String args[] )
	{
		double x=Double.parseDouble(args[0]);
		double y=Double.parseDouble(args[1]);
		double sum=0;
		double sub;
		double mul;
		double div;
		sum=x+y;
		sub=x-y;
		mul=x*y;
		div=x/y;
		System.out.println("sum="+sum);
		System.out.println("sub="+sub);
		System.out.println("multiplication="+mul);
		System.out.println("division="+div);
	}
}