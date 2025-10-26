class Bank {
public:
    // call copy constructor of vector using initialization list
    Bank(vector<long long>& balance) : bank(balance), n(balance.size()) { }
    
    bool transfer(int account1, int account2, long long money) {
        if (account1 < 0 || account1 > this->n) {
            return false;
        }
        if (account2 < 0 || account2 > this->n) {
            return false;
        }
        if (withdraw(account1, money)) {
            deposit(account2, money);
            return true;
        }
        return false;
    }
    
    bool deposit(int account, long long money) {
        if (account < 0 || account > this->n) {
            return false;
        }
        this->bank[account - 1] += money;
        return true;
    }
    
    bool withdraw(int account, long long money) {
        if (account < 0 || account > this->n) {
            return false;
        }
        if (money <= this->bank[account - 1]) {
            this->bank[account - 1] -= money;
            return true;
        }
        return false;
    }
private:
    std::vector<long long> bank;
    int n;
};


/**
 * Your Bank object will be instantiated and called as such:
 * Bank* obj = new Bank(balance);
 * bool param_1 = obj->transfer(account1,account2,money);
 * bool param_2 = obj->deposit(account,money);
 * bool param_3 = obj->withdraw(account,money);
 */

