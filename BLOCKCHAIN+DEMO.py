
# coding: utf-8

# # BLOCKCHAIN DEMO

# ## Class Block to create objects for all the class

# In[176]:


import hashlib

class Block():
    
    def __init__(self,previousHash,transactions):
        self.previousHash = previousHash
        self.transactions = transactions
    
    def getBlockHash(self):
        Hash = hashlib.sha1()
        Hash.update(str.encode(self.transactions) + str.encode(self.previousHash))
        return Hash.hexdigest()
    
    #def transactions(self):
        #print(Block.transactions)
    
    #def previoushash(self):
        #print(Block.previousHash)


# In[168]:


GenesysBlock = Block(previousHash="0",transactions = "rohit gives manvi 1000 coins")


# In[169]:


Block_1 = Block(GenesysBlock.getBlockHash(),transactions = "manvi gives rohit 50 coins")
Block_2 = Block(Block_1.getBlockHash(),transactions = "shivam gives manvi 10 coins")
Block_3 = Block(Block_2.getBlockHash(),transactions = "vaibhav gives shivam 50 coins")
Block_4 = Block(Block_3.getBlockHash(),transactions = "rohin gives rohit 20 coins")
Block_5 = Block(Block_4.getBlockHash(),transactions = "raunak gives manvi 90 coins")


# In[170]:


GenesysBlock.getBlockHash()


# In[171]:


Block_1.getBlockHash()


# In[172]:


Block_2.getBlockHash()


# In[173]:


Block_3.getBlockHash()


# In[174]:


Block_4.getBlockHash()

