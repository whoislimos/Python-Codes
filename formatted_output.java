import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
            System.out.println("================================");
            int n = 15;
            for(int i=0; i<3; i++){
                String s1=sc.next();
                int x=sc.nextInt();
                //Complete this line
                System.out.print(s1);
                    for(int j=0; j<(n - s1.length()); j++){
                        System.out.print(" "); 
                    }
                if(String.valueOf(x).length() < 3){
                    for(int k=3; k >String.valueOf(x).length(); k--){
                        System.out.print("0");
                    }
                }
                System.out.println(x);                
            }
            System.out.println("================================");

    }
}


/*

================================
hello          000
hackerrank     065
java           010
================================


*/
