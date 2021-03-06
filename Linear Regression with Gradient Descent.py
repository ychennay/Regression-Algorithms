// taken from different open source pieces of code available on the internet,
// including: http://www.ozzieliu.com/2016/02/09/gradient-descent-tutorial/#gradient-descent
// I have corrected certain typos within the code to make the gradient descent algorithm run smoothly
#%%
importfilepath = "C:/Users/ychennay/Documents/Python Scripts/Toy Data.csv"

data = pd.read_csv(importfilepath)

data['Intercept'] = 1
y = data['Salary']
X= data[['Age', 'Intercept']]

X= np.array(X)
y = np.array(y)
beta = np.array([0,0])

def cost_function(X, y, beta):
    m = len(y)
    J = np.sum((X.dot(beta)-y)**2)/2/m
    return J

iterations = 10000
learningrate = .0001
beta = np.array([0,0])
cost_history = [0] * iterations

for i in range(iterations):
    hypothesis=X.dot(beta)
    loss = hypothesis - y
    gradient = X.T.dot(loss)/m
    beta = beta.T - learningrate * gradient
    cost= cost_function(X,y,beta)
    cost_history[i] = cost    
    i = i+1

#display the first 50 results
for i in range(50):
    print("Cost", cost_history[i])    

#print final coefficients
    beta
