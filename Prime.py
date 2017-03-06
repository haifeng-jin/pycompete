class PrimeNumber:
    def __init__(self):
        self.MAXN=1000
        self.notprime=self.MAXN*[False] # notprime is a table, false is prime number
        self.prime=(self.MAXN+1)*[0] # prime store the number of prime


    #judge where a number<MAXN is a prime or not
    def isPrime(self,n):
        self.notprime[0]=self.notprime[1]=True
        for i in range(2,self.MAXN):
            if not self.notprime[i]:
                if i>self.MAXN/i:## in case of i* i is overflow
                    continue
                # start from i*i, number smaller than i*i have already sieved,
                j=i*i
                while j<self.MAXN:
                    self.notprime[j]=True
                    j+=i
        return not self.notprime[n]


    # get number of prime whose value is <=n
    #n should be smaller or equal to self.MAXN
    #return the number of prime whose value <=n
    def getPrime(self,n):
        for i in range(2,n+1):
            if self.prime[i]==0:
                self.prime[0]+=1
                self.prime[self.prime[0]]=i
            j = 1
            while j <= self.prime[0] and self.prime[j] <= n / i:
                self.prime[self.prime[j] * i] = 1
                if i % self.prime[j] == 0:
                    break
                j += 1
        #print(self.prime[1:self.prime[0]+1])
        return self.prime[0]



if __name__ =="__main__":
    pn=PrimeNumber()
    index=1
    for i in range(0,150):
        if pn.isPrime(i):
            print(index,i,sep=' ')
            index+=1
    print(pn.getPrime(150))

