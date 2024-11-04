def findDecision(obj): #obj[0]: 0, obj[1]: 1, obj[2]: 2, obj[3]: 3, obj[4]: 4, obj[5]: 5, obj[6]: 6
   # {"feature": 0, "instances": 398, "metric_value": 0.9877, "depth": 1}
   if obj[0]>-5.565735898981081:
      # {"feature": 1, "instances": 397, "metric_value": 0.9871, "depth": 2}
      if obj[1]>-7.77585280424806:
         # {"feature": 2, "instances": 396, "metric_value": 0.9865, "depth": 3}
         if obj[2]>-4.34191581326578:
            # {"feature": 5, "instances": 395, "metric_value": 0.986, "depth": 4}
            if obj[5]>-3.511878193549121:
               # {"feature": 3, "instances": 394, "metric_value": 0.9854, "depth": 5}
               if obj[3]<=4.240777195860392:
                  return 'B'
               elif obj[3]>4.240777195860392:
                  return 'B'
               else:
                  return 'B'
            elif obj[5]<=-3.511878193549121:
               return 'M'
            else:
               return 'B'
         elif obj[2]<=-4.34191581326578:
            return 'M'
         else:
            return 'B'
      elif obj[1]<=-7.77585280424806:
         return 'M'
      else:
         return 'B'
   elif obj[0]<=-5.565735898981081:
      return 'M'
   else:
      return 'B'
