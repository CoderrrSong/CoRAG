import json

# 读取JSON文件
with open("data_v12/Pop/train_labels.json", "r") as f:
    data = json.load(f)

# 处理每个元素的labels
for item in data:
    if "labels" in item:
        # 将每个标签包装成单元素列表
        item["labels"] = [[x] for x in item["labels"]]

# 保存结果
with open("data_v12/Pop/train_labels_list.json", "w") as f:
    json.dump(data, f, indent=2)

print("转换完成，结果已保存到train_labels_list.json")
