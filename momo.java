import java.io.*;
import java.util.Scanner;
class momo
{
public static void main(String args[]){
Scanner sc =new scanner(System.in);
strinsg s=sc.nextLine();
int c=1;
for(int i=0;i<s.length()-1;i++){
if((s.charAt(i)==' ') || (s.chaeAt(i+1)!=' '))
c++;
}
System.out.println(c);
}
}
