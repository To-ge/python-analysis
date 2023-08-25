import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score

# df = pd.read_csv('pull-requests.csv', sep='\t')
df = pd.read_csv('test.csv', header=None, names=['Line', 'Merged'])
# データの準備（例）
# X = df[['Number', 'Title', 'State', 'User']]
# y = df[['Merged']]

# df['Merged'] = df['Merged'].map({'True': 1, 'False': 0})

X = df[['Line']]
y = df[['Merged']]
print(X)
print('🚀')
print(y)
# データの前処理（例）
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    random_state=42)

# モデルの構築
model = LogisticRegression()

# モデルの学習
model.fit(X_train, y_train)

# モデルの評価
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)

# 新しいPRの特徴量を抽出
# new_pr_features = データの特徴量
#
# # 予測の実行
# prediction = model.predict(new_pr_features)
# if prediction == 1:
#     print("PRはマージされると予測されました。")
# else:
#     print("PRはマージされないと予測されました。")
