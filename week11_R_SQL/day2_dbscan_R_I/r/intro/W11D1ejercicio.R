# para el ejercicio de hoy copia las siguientes líneas en tu script
# RECUERDA instalar el paquete tidyverse
library(tidyverse)
# cargamos los datos
data("mtcars")
head(mtcars)

# limpio los datos
datos_limpios <- mtcars %>%
  filter(cyl == 4)

# grafico los datos
plot(x = mtcars$wt, y = mtcars$mpg)
