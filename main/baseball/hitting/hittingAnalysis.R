library(ggplot2)

#hitting already a presaved value on there

#I can create an RMd file that uses knitr to display the output



#Plotting pie chart
## As more data is collected, pie chart will be more refined ##
ggplot(hitting, aes(x="", y = Outs, fill = Zone)) + 
   geom_bar(stat="identity", width=1, color="white") + 
   coord_polar("y", start=0) + 
   theme_void()
