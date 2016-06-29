class Solution {
public:
    int reverse(int x) {
        if (x==0) return x;
        
        std::stack<int> digits;
        int value = std::abs(x);
        int n = 0;
        while (value > 0){
            value = value/10;
            digits.push(value%10);
            n++;
        }
        
        value = 0;//reset value
        for(int i=0;i<n;i++){
            value += digits.pop() * myPow(10, n);
        }
        
        return x>0 ? value : -value;
    }
private:
    int myPow(int base, int pow){
        while (pow-- > 0) base *= pow;
        
        return base;
    }
};