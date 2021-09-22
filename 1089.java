import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{

  public static void main (String[] args) throws IOException{
    InputStreamReader go = new InputStreamReader(System.in);
    BufferedReader reader = new BufferedReader(go);

    int n = Integer.parseInt(reader.readLine());

    while(n > 0){

      String[] initial_data = reader.readLine().split(" ");
      int[] data = new int[n];

      for(int i = 0; i < n; i++){
      	data[i] = Integer.parseInt(initial_data[i]);
      }

      boolean down = false;
      boolean last = false;

      if(data[n-1] > data[0]){
      		last = true;
      }

      int peeks = 0;

      for(int j= 0; j < n-1; j++){
      	
      	if(data[j] > data[j+1]){
      		down = true;
      	} else {
      		down = false;
      	}

      	if(last != down){
      		peeks++;
      	}

      	last = down;
      }

      if(data[n-1] > data[0]){
      	down = true;
      } else {
      	down = false;
      }

      if(last!= down){
      	 peeks++;
      }

       System.out.println(peeks);
       n = Integer.parseInt(reader.readLine());

    }
  }
}