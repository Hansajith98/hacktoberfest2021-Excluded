class Solution {
public int findDuplicate(int[] a) {
  int i=0, j=0, temp=0;
  for(i=0;i<a.length;){
      if(i>=a.length || temp>=a.length){
          break;
      }
      if(a[i]==i+1){
          i++;
      }
      else{
          j = a[i];
          if(j<i){
              a[i] = a[a[i]-1];
              a[j-1] = j;
          }
          else{
              a[i] = a[a[i]];
              a[j] = j;
          }
          temp++;
      }
  }
  return a[i];
}
}