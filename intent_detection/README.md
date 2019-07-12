model có tên là intent_model.bin với link drive là https://drive.google.com/file/d/1CG1atus1Oqn4E-9LHSScEB0HbEVShEhE/view?usp=sharing
tải về đặt tại địa chỉ "intent_detection_chatbot/intent_detection/intent_model.bin"
------------------------------------------------------------------------------------
trong file intent.py có 2 hàm đó là:
+ load_model(): trả về giá trị là model đã load
+ get_intent(validation): tham số là model trong một biến chung mà không cần load lại model.
khi gọi hàm thì sẽ yêu cầu nhập input và xuất ra output là nhãn
trong trương trình đặt 1 biến toàn cục  validation=load_model() để load model và sử dụng cho cả chương trình
hàm get_intent( validation) có tham số  validation chính là biến này 


