import java.io.DataInputStream;
class factorial
{
	public static void main(String args[])
	{
		int i;
		DataInputStream x=new DataInputStream(System.in);
		System.out.println("enter the value");
		int fact=1;
		try
		{
			int n=Integer.parseInt(x.readLine());
			for(i=1;i<=n;i++)
			{
				fact=fact*i;
				System.out.println(fact);
			}
		}
		catch(Exception e){}
	}
}