###MAP
~~~bash
# 声明　
declare -A animals
# 定义　
animals=( ["moo"]="cow" ["woof"]="dog")

declare -A animals=( ["moo"]="cow" ["woof"]="dog")

#获取value 
${animals[@]}
#
获取keys 

${!animals[@]}
~~~


