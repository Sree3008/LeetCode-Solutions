class Solution {
    public char findTheDifference(String s, String s1) {
		char[] arr=s.toCharArray();
		char[] arr1=s1.toCharArray();
		for(int i=0;i<arr1.length;i++){
		    boolean b=false;
		    for(int j=0;j<arr.length;j++){
		        if(arr1[i]==arr[j]){
                   arr[j]='#';
		            b=true;
		            break;
		        }
		        
		    }
		    if(!b){
		        return arr1[i];
		        }
		}
        
        return 0;

    }
}

