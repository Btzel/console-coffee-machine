# Console Coffee Machine

A Python-based console application simulating a coffee vending machine with resource management and payment processing.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Console](https://img.shields.io/badge/Console-Application-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🎯 Overview

This project implements a console-based coffee machine that:
1. Manages drink recipes and resources
2. Processes coin-based payments
3. Tracks inventory levels
4. Provides reporting functionality

## ☕ Available Drinks

| Drink      | Water (ml) | Milk (ml) | Coffee (g) | Cost ($) |
|------------|------------|-----------|------------|----------|
| Espresso   | 50         | -         | 18         | 1.50     |
| Latte      | 200        | 150       | 24         | 2.50     |
| Cappuccino | 250        | 100       | 24         | 3.00     |

## 🔧 Features

### Resource Management
- Water tracking
- Milk inventory
- Coffee bean monitoring
- Money collection

### Payment System
- Accepts multiple coin types:
  - Quarters ($0.25)
  - Dimes ($0.10)
  - Nickles ($0.05)
  - Pennies ($0.01)
- Calculates and returns change
- Validates payment sufficiency

### System Commands
- `report`: View current resource levels
- `off`: Turn off the machine
- Drink selection menu

## 🛠️ Technical Components

### Resource Handling
- Resource sufficiency checking
- Inventory updates
- Resource reporting

### Payment Processing
- Coin counting
- Change calculation
- Transaction validation

### User Interface
- ASCII art logo
- Interactive menu system
- Status messages
- Error handling

## 🚀 Usage

1. Run the program:
```bash
python main.py
```

2. Select a drink:
```
What would you like? (espresso/latte/cappuccino):
```

3. Insert coins when prompted:
```
Please insert coins.
How many quarters?:
How many dimes?:
How many nickles?:
How many pennies?:
```

4. Check resource levels:
```
> report
Water: 3000ml
Milk: 2000ml
Coffee: 1000g
Money: $0
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Author

- Burak TÜZEL 

