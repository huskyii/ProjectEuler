/* author jiang
 * email   mail.jiang.cn@gmail.com
 * created on 2014-5-28
 */

#include <stdio.h>
#include <string.h>

int solve(){
  int tmp[600],res = 0;
  memset(tmp,0,sizeof(tmp));
  int index = 0;
  for(int i = 1; (i*3) < 1000; ++i){
    tmp[index] = i*3;
    index++;
    if(i*5 < 1000 && i*5 % 3 != 0){
      tmp[index] = i*5;
      index++;
    }
  }
  for(int i = 0; tmp[i] != 0; i++){
    res += tmp[i];
  }
  return res;
}

int main(void){
  printf("%d",solve());
  return 0;
}
