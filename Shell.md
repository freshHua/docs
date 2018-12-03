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

###getopt

~~~bash

ARGS=$(getopt -o b: -l branch: -- "$@")`
eval set -- "$ARGS"
while [ -n "$1" ]; do
    case "$1" in
        -b|--branch) branch=$2; shift 2;;
        *) break;;
    esac
done

#注： -o 短变量名
     -l 长变量名
	 ： 需要复制
~~~
