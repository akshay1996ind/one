import java.util.*;
class Wantboy
{
  public static void main(String[] args)
  {
    int family = 1;
    int boys = 0;
    int girls = 0;
    int n = 0;
    int g=0;
    int b=0;
    int end=0;

    for(int i = 100;i>0;i--)
    {
     while(end==0)
      {
        end =0;
        int child = born();
        //System.out.println(child);
        if(child==0)
        {
          System.out.println("girl");
          girls++;
          g++;
          i++;
        }
        else
        {
          System.out.println("boy");
          boys++;
          b++;
          if(b==1)
          {
            int secondchild = born();
            if(secondchild == 0)
            {
              System.out.println("girl-y");
              girls++;
              g++;
            }
            else
            {
              System.out.println("boy-y");
              boys++;
              b++;
            }
            end=1;
           family++;
          }
        }
      System.out.println(family+" "+b+" "+g);
        g = 0;
        b = 0;
      }
    }
    try
    {
     System.out.println(boys);
     Thread.sleep(3000);
     System.out.println(girls);
    }
   catch(InterruptedException e)
   {
     System.out.println("got interrupted!");
       }
  }
  public static int born()
  {
    Random rand = new Random();
    int birth = rand.nextInt(2);
    return birth;
  }

}
