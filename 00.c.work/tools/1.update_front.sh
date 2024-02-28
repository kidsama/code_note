#!/bin/bash
set -e

branch_array=("工行" "主线" "太保" "海关" "香港警察")
length=${#branch_array[@]}
update_branch=""

function update_front(){
  case $1 in
  0)
    file_path="/home/liu/clone_node/ICBC/monitor-view/";;
  1)
    file_path="/home/liu/clone_node/main/monitor-view-restructure/";;
  2)
    file_path="/home/liu/clone_node/taibao/monitor-view/";;
  3)
    file_path="/home/liu/clone_node/NTP/monitor-view-restructure/";;
  4)
    file_path="/home/liu/clone_node/xgjc/monitor-view-restructure/";;
  *)
    echo "参数错误，可用参数如下：0,1,2,3,4"
    exit 1
  esac

  s_time=$(date +%s)
  cd $file_path || exit
  pull_res=$(git pull)
  if [ "$pull_res" = "已经是最新的。" ];then
    echo "${branch_array[$1]}$pull_res"
  else
    update_branch="$update_branch ${branch_array[$1]}"
    npm run build
  fi
  e_time=$(date +%s)
  cost_time=$((e_time-s_time))
  echo "耗时：$cost_time"
}

echo "$(date +'%Y-%m-%d %H:%M:%S')=============================="
~/anaconda3/envs/liu/bin/python /data/lwx984502/myscript/wx/send_wx.py "$(date +'%Y-%m-%d %H:%M:%S')开始更新"

for ((i = 0; i < length; i++)); do
  echo "${i}.更新${branch_array[$i]}代码..."
  update_front "${i}"
done

~/anaconda3/envs/liu/bin/python /data/lwx984502/myscript/wx/send_wx.py "$(date +'%Y-%m-%d %H:%M:%S')更新完成: $update_branch"