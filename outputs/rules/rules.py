def findDecision(obj): #obj[0]: sepal_length, obj[1]: sepal_width, obj[2]: petal_length, obj[3]: petal_width
   # {"feature": "petal_length", "instances": 105, "metric_value": 1.5822, "depth": 1}
   if obj[2]>1.9431970926890703:
      # {"feature": "petal_width", "instances": 68, "metric_value": 0.9975, "depth": 2}
      if obj[3]<=1.7:
         # {"feature": "sepal_length", "instances": 35, "metric_value": 0.5127, "depth": 3}
         if obj[0]<=7.0:
            # {"feature": "sepal_width", "instances": 34, "metric_value": 0.4306, "depth": 4}
            if obj[1]<=2.8:
               return 'Iris-versicolor'
            elif obj[1]>2.8:
               return 'Iris-versicolor'
            else:
               return 'Iris-versicolor'
         elif obj[0]>7.0:
            return 'Iris-virginica'
         else:
            return 'Iris-versicolor'
      elif obj[3]>1.7:
         # {"feature": "sepal_length", "instances": 33, "metric_value": 0.1959, "depth": 3}
         if obj[0]>5.9:
            return 'Iris-virginica'
         elif obj[0]<=5.9:
            # {"feature": "sepal_width", "instances": 6, "metric_value": 0.65, "depth": 4}
            if obj[1]<=3.0:
               return 'Iris-virginica'
            elif obj[1]>3.0:
               return 'Iris-versicolor'
            else:
               return 'Iris-virginica'
         else:
            return 'Iris-virginica'
      else:
         return 'Iris-virginica'
   elif obj[2]<=1.9431970926890703:
      return 'Iris-setosa'
   else:
      return 'Iris-setosa'
