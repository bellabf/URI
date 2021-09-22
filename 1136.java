import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{

  public static void main (String[] args) throws IOException{
    InputStreamReader go = new InputStreamReader(System.in);
    BufferedReader reader = new BufferedReader(go);

    

     String[] initial_data = reader.readLine().split(" ");
     int n = Integer.parseInt(initial_data[0]);
     int b = Integer.parseInt(initial_data[1]);

     while(n>0){
	     int[] number = new int[b];
	     boolean[] remaining = new boolean[n+1];

	     String[] tobecalled = reader.readLine().split(" ");

	     for(int i = 0; i < b; i++){
	     	number[i] = Integer.parseInt(tobecalled[i]);
	     }

	     for(int i = 0; i < n; i++){
	     	remaining[i] = false;
	     }

	     for(int i=0; i < b; i++){
	     	for(int j =0; j <b; j++){
	     		int test = number[i] - number[j];
	     		if( test >= 0 && test < n+1){
					remaining[test] = true;
	     		}
	     	}
	     }

	     boolean all_possible = true;
	     for(int i = 0; i < n+1; i++){
	     	all_possible = all_possible && remaining[i];
	     	if(!all_possible){
	     		break;
	     	}
	     }

	     if(all_possible){
	     	System.out.println("Y");
	     }else{
	     	System.out.println("N");
	     }

	    initial_data = reader.readLine().split(" ");
    	n = Integer.parseInt(initial_data[0]);
     	b = Integer.parseInt(initial_data[1]);
	}     
  }
}