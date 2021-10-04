class Tree 
{
    int getCount(Node node, int low, int high) 
    {  
        if(node == null) 
            return 0; 
    	if (node.data == high && node.data == low)
    		return 1;
        if(node.data >= low && node.data <= high) 
            return 1 + this.getCount(node.left, low, high)+ 
                this.getCount(node.right, low, high); 
        else if(node.data < low) 
            return this.getCount(node.right, low, high); 
        else
            return this.getCount(node.left, low, high);      
    } 
}
