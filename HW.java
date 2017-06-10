
package cogs9;

import java.io.*;
import java.util.*;



import java.io.FileNotFoundException;
public class HW {
	 public static void main(String arg[]) throws Exception
	    {
		   
	        String fileNameDefined = "DATA1.csv";
	        // -File class needed to turn stringName to actual file
	        File file = new File(fileNameDefined);
	        List<String> set = new ArrayList<String>();
	        try{
	            // -read from filePooped with Scanner class
	            Scanner inputStream = new Scanner(file);
	            // hashNext() loops line-by-line
	            while(inputStream.hasNext()){
	                //read single line, put in string
	                String data = inputStream.nextLine();
	               if(!data.endsWith(",,,")){
	                set.add(data);
	                }

	            }
	            System.out.println(set.size());
	            // after loop, close scanner
	            FileWriter fileWriter = null;
	            final String NEW_LINE_SEPARATOR = "\n";
	            fileWriter = new FileWriter("DATAOUT.csv");

	            for(int i=0;i<set.size();i++){
	            	System.out.println(set.get(i));
	            	fileWriter.append(String.valueOf(set.get(i))); fileWriter.append(NEW_LINE_SEPARATOR);

	            }
	            inputStream.close();


	        }catch (FileNotFoundException e){

	            e.printStackTrace();
	        }

	    }
	}
	    