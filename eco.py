import numpy as np
import matplotlib.pyplot as plt

print("---Microeconomics: Break Even Analysis---")
fc= float(input("Enter fixed costs"))
vc=float(input("Enter variable cost per unit:"))
sp=float(input("Enter selling price per unit:"))
mp=int(input("Enter max production units to visualize:"))
q = np.linspace(0, mp, 100)
tc=fc+(vc*q)
tr=sp*q

# Find the Break-even point (Quantity where Revenue = Cost)
# Q = Fixed Costs / (Price - Variable Cost)
beq=fc/(sp-vc)
bev=sp*beq

# Plotting the Cost and Revenue lines
plt.figure(figsize=(10, 6))
plt.plot(q,tc,label="total cost",color="red",linewidth=2)
plt.plot(q,tr,label="total revenue",color="blue",linewidth=2)
# Highlighting the Break-even Point
plt.plot(beq, bev, 'ko') # 'ko' makes a black dot
plt.title("Economic Break-Even Analysis", fontsize=14)
plt.xlabel("Quantity of Units Produced", fontsize=12)
plt.ylabel("Money (USD)", fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
print("\nAnalysis Result:")
print("To breakeven you mus sell between", beq , "units")
print("Revenue at breakeven", bev)

plt.show()
