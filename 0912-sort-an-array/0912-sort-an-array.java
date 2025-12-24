class Solution {
    public int[] sortArray(int[] nums) {
        Divide(nums,0,nums.length-1);
        return nums;
    }
    public void Divide(int [] nums,int low,int high){
        if(low>=high)return;
        int mid = (low+high)/2;
        Divide(nums,low,mid);
        Divide(nums,mid+1,high);
        Merge(nums,low,mid,high);
    }
    public void Merge(int []nums,int low,int mid,int high){
        int merged[] = new int[high-low+1];
        int i = low;
        int j = mid+1;
        int x = 0;
        while(i<=mid && j<=high){
            if(nums[i]<=nums[j]){
                merged[x++] = nums[i++];
            }
            else{
                merged[x++] = nums[j++];
            }
        }
        while(i<=mid){
           merged[x++] = nums[i++]; 
        }
        while(j<=high){
           merged[x++] = nums[j++];
        }
        for(int k = 0;k<merged.length;k++){
            nums[low+k] = merged[k];
        }
    }
}