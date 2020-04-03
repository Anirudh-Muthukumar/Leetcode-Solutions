class Solution {
public:
    
    bool isHappy(int n) {
        int max_iter = 6;
        int sum = 0, temp = n, dgt;
        while(sum!=1)
        {
            sum = 0;
            while(temp) {
                dgt = temp%10;
                sum += dgt * dgt;
                temp /= 10;
            }
            max_iter-=1;
            if (max_iter==0)
                break;
            temp = sum;
        }
        return sum==1;
    }
};