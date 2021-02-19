# Covid-19_Predictor

PROPHET is a web application that contains front-end and back-end implementation in a very-beginning stage. It aims to provide a trend prediction of COVID-19 for both Regions and Buildings. The prediction of the trend of COVID-19 can help us to determine which kind of preventions and control strategies are more efficient.

## Welcome Page

![Homepage](../cityhack/doc/images/Homepage.png)

## Regions Prediction

### Overview

![Overview](../cityhack/doc/images/Region_Overview.png)

### Visualizations

![Details](../cityhack/doc/images/Region_details.png)

### Set Parameters

![Para](../cityhack/doc/images/Region_Parameter.png)

All parameters can be set before the prediction is started. When the visualiztion is running, you can pause at any time and change some parameters, which is like some policies are adopted in the real world, then you can view the trend after the 'policies' are adopted. 

### Data Export

After the prediction, you can download the raw data derived by our model, and do further analyses. 
![Data](../cityhack/doc/images/Data_Export.png)

### How it works

A modified SEIR Model Design is shown below: 
![Model](../cityhack/doc/images/Model.png)

### Parameters Meanings
![Explanation](../cityhack/doc/images/Explanation.png)

### Calulations
![Equation](../cityhack/doc/images/Equation.png)



# Frontend

## Project setup
```
yarn install
```

### Compiles and hot-reloads for development
```
yarn serve
```

### Compiles and minifies for production
```
yarn build
```

### Run your end-to-end tests
```
yarn test:e2e
```

### Lints and fixes files
```
yarn lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

# Backend server

## Install dependency

```
npm install
```

## Makesure you installed dependency for following items
```
import sys
import math
import json
import numpy as np
from scipy.integrate import odeint
```
## Run server

```
node app.js
```