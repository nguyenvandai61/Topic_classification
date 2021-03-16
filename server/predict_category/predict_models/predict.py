#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from predict_category.predict_models.data_preparation import NLP, FileStore, FileReader
from newspaper import Article
import numpy as np

def predict_category(url):
    lr = pickle.load( open( "predict_category/predict_models/model_logis_new.pkl", "rb" ) )
    tfidf = pickle.load( open( "predict_category/predict_models/tfidf_new.pkl", "rb" ) )
    # url = input('Nhap vao url: ')
    article = Article(url)
    article.download()
    article.parse()
    text = article.text + ' ' + article.title
    # text = 'Phiến đá khảm 2.000 năm tuổi này từng được thực hiện để lát trên sàn con tàu do Hoàng đế La Mã Caligula yêu cầu thực hiện vào khoảng năm 40 sau Công nguyên.\n\nPhiến đá khảm 2.000 năm tuổi này từng được thực hiện để lát trên sàn con tàu do Hoàng đế La Mã Caligula yêu cầu thực hiện vào khoảng năm 40 sau Công nguyên.\n\nPhiến đá khảm này sau quá trình chìm nổi đã có một quãng thời gian khá dài trở thành mặt bàn uống nước trong một gia đình sống ở thành phố New York (Mỹ). Sau khi được phát hiện ra nguồn gốc xuất xứ thực sự, phiến đá đặc biệt này đã được đưa trở về đúng vị trí của nó trong tuần qua.\n\nKể từ nay, phiến đá này sẽ được lưu giữ trong Bảo tàng Tàu thuyền La Mã, bảo tàng này được xây dựng hồi thập niên 1930 để trưng bày những hiện vật quý giá còn lưu giữ được từ hai con tàu lớn mà Hoàng đế La Mã Caligula từng yêu cầu thực hiện vào khoảng năm 40 sau Công nguyên. Mục đích của hai con tàu này không phải là để phục vụ hoạt động đi lại mà là để trở thành hai tòa lâu đài nổi trên hồ Nemi.\n\nSau này, cả hai con tàu đều bị đắm nhưng đã được trục vớt lên từ đáy hồ Nemi vào cuối thập niên 1890. Phiến đá khảm có diện tích 1,5 mét vuông với những họa tiết hình học màu xanh, đỏ, và trắng này đã từng là một phần đá lát sàn trên một trong hai con tàu được đóng khi ấy.\n\nHai con tàu từng được thiết kế và thực hiện với ý tưởng như thể hai tòa lâu đài nổi trên mặt nước, như là minh chứng cho quyền lực của Hoàng đế Caligula và đế chế La Mã.\n\nHiện tại, thông tin về hành trình chìm nổi của phiến đá vẫn còn nhiều điều chưa được làm rõ.\n\nHiện tại, thông tin về hành trình chìm nổi của phiến đá vẫn còn nhiều điều chưa được làm rõ. Chỉ biết rằng sau cùng nó đã được một nhà sưu tầm đồ cổ sống tại New York mua lại và biến thành mặt bàn uống nước trong nhà suốt hàng thập kỷ.\n\nCho tới năm 2013, chuyên gia trong lĩnh vực đá tự nhiên và đá hoa cương đến từ nước Ý - ông Dario Del Bufalo thực hiện một buổi ký tặng sách, nhân dịp ông cho ra mắt cuốn sách mới có đề cập tới cả những loại đá từng được các vị Hoàng đế La Mã ưa chuộng. Sự kiện có sự tham gia của những vị khách đến từ New York (Mỹ).\n\nKhi ông đang thực hiện việc ký tặng sách, có hai người phụ nữ xem sách của ông rồi nói: \"Đây là mặt bàn nhà Helen mà\". Hai người phụ nữ vừa nhìn một bức ảnh xuất hiện trong cuốn sách mới ra mắt vừa nói như vậy, bức ảnh trong sách chụp một phiến đá khảm đang được trưng bày tại Bảo tàng Tàu thuyền La Mã nằm gần hồ Nemi (Ý).\n\nÔng Dario Del Bufalo lại gần và hỏi kỹ hơn xem Helen là ai và họ đang nói về cái gì. Hóa ra, họ đang nói về một người phụ nữ chuyên sưu tầm đồ cổ có tên Helen Fioratti, bà Helen đã mua được một phiến đá vốn dùng để lát sàn trên con tàu của Hoàng đế La Mã Caligula, bà dùng phiến đá này làm mặt bàn uống nước trong nhà mình.\n\nMột số hiện vật còn lại của hai con thuyền huyền thoại\n\nHồ Nemi (Ý)\n\nHai người phụ nữ đến dự buổi ký tặng sách đã nhớ ra phiến đá đặc biệt ấy ở nhà bà Helen, họ chia sẻ những thông tin cho ông Dario Del Bufalo.\n\nSau này, bà Helen bị cảnh sát tại New York điều tra vì nghi ngờ có liên quan tới việc cổ vật bị đánh cắp khỏi nước Ý.\n\nPhiến đá này đã bị cảnh sát thu giữ vào tháng 10/2017 để gửi trả về nước Ý. Tới tuần qua, phiến đá chính thức được đưa trả về Bảo tàng Tàu thuyền La Mã để được trưng bày bên cạnh những hiện vật khác của hai con tàu từng được Hoàng đế Caligula yêu cầu thực hiện.\n\nNgười phụ nữ từng mua phiến đá này về làm mặt bàn uống nước - bà Helen Fioratti từng chia sẻ với báo chí rằng bà đã mua phiến đá từ hơn 40 năm trước. Bà mua phiến đá từ khi còn sống ở nước Ý và được người ta giới thiệu là phiến đá từng thuộc về một gia đình quý tộc tại Ý.\n\nBà Helen Fioratti không gặp bất cứ rắc rối pháp lý nào và cũng chấp nhận việc bị tịch thu phiến đá: \"Tôi từng được môi giới bởi một chuyên gia nghệ thuật người Ý. Tôi đã rất vui với việc mua được phiến đá ấy, thực sự yêu thích nó. Chúng tôi đã có nhiều năm sử dụng nó và những khách đến nhà đều khen ngợi vẻ đẹp của chiếc bàn nhờ có phiến đá đó\".\n\nBích Ngọc\n\nTheo Daily Mail'
    nlp = NLP(text)

    text = [' '.join(nlp.preprocessText(text))]
    if text != ['']:
        value_test = tfidf.transform(text)

        idx = lr.predict(value_test)[0]
        valArr = lr.predict_proba(value_test)
        valS = np.array(valArr)
        np.set_printoptions(suppress=True)
        
        tem = dict(zip(lr.classes_,valArr[0]))
        res = dict(sorted(tem.items(), key = lambda item:item[1], reverse = True))
        return res
        # print(valArr)
        # print(lr.classes_)
    else:
        return None
        print('Error in read the article')

print(predict_category('https://vnexpress.net/kia-ev6-crossover-coupe-dien-ra-mat-4248428.html'))