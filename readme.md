## Running the containers

***須確認環境中已安裝Docker及Docker-Compose，才能依以下指令建立服務。***

取得原始碼後於docker-compose.yml所在位置執行以下指令，即可建置並執行Docker container:

    [sudo] docker-compose build
    [sudo] docker-compose up 

## Testing

本地測試使用127.0.0.1。若要從用戶端連入服務器測試，需將myproject/app.py第22行之ip參數值由127.0.0.1改為服務器對外ip後即可。

測試範例：
-   取得短網址：使用GET將欲縮短之原網址做為url參數傳入ShortUrl API中，API會返回短網址。
`curl http://127.0.0.1/ShortUrl?url=https://www.itread01.com/study/python3-tutorial.html`

- 使用GET返回之短網址，即會導向原始網址。
 `   curl http://127.0.0.1/F`
