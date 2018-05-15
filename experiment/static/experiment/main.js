String.prototype.format = function() {
  a = this;
  for (k in arguments) {
    a = a.replace("{" + k + "}", arguments[k])
  }
  return a
}
EXPCNT = 10
function genchoice(i1, i2) {
	correctAt = Math.floor(Math.random() * 4)
	ret = [0,0,0,0];
	for(i=0;i<4;i++) {
		if(correctAt == i) {
			ret[i] = i1*i2;
			continue;
		}
		t = Math.floor(Math.random()*8);
		if(t==0)
			ret[i] = (i1-1)*i2;
		else if(t == 1)
			ret[i] = (i1+1)*i2;
		else if(t == 2)
			ret[i] = i1*(i2-1);
		else if(t == 3)
			ret[i] = i1*(i2+1);
		else if(t == 4)
			ret[i] = i1*i2-1;
		else if(t == 5)
			ret[i] = i1*i2+1;
		else if(t == 6)
			ret[i] = i1*i2+2;
		else if(t == 7)
			ret[i] = i1*i2+5;
	}
	return ret;
}
lastclick = -1;
function mainexp() {
	data = {'questions':[],'answeredTime':[],'iscorrect':[]}
	ils = Array(10).keys()
	console.log(lis);
	ils.map(i => {
		i1 = Math.round(Math.random()*12+3);
		i2 = Math.round(Math.random()*13+2);
		ans = i1 * i2;
		choices = genchoice(i1, i2);
		data['questions'].push("{0} {1}".format(i1, i2));
		console.log("i1={0}, i2={1}".format(i1, i2));
		$('#question')
			.text("{0}&times;{1}=??".format(i1, i2));
		arr = [0,1,2,3];
		pms = arr.map((j) => {
			return new Promise((resolve, reject) => {
				$('#btn'+ j)
					.text(choices[j])
					.on('click', () => {resolve(j)});		
				});			
			})
		Promise.any(pms).then((lastclick) => {
			if(ans == choices[lastclick]) {
				data['iscorrect'].push(1);
			} else {
				data['iscorrect'].push(0);
			}
			data['answeredTime'].push(timecnt);
		});
	})
	$('#infotext')
		.text('실험이 종료되었습니다! 잠시 후 자동으로 다음 화면으로 넘어갑니다.');
	$('.exprow')
		.addClass('hide');
	$('#mainbtn')
		.removeClass('hide');
	$('#maindata')
		.val(JSON.stringify(data));
	setTimeout(function() {
		$('#mainform').submit();	
	}, 1500);		
};
timecnt = 0;
$( document )
	.ready( function() {
		$('#mainbtn').click(function() {
			$('.exprow')
				.removeClass('hide');
			$('#infotext')
				.text('실험이 진행중입니다.')
			$(this)
				.text('실험 종료')
				.off('click')
				.addClass('hide');
			var id = setInterval(function() {
				timecnt++;
				min = String(Math.floor(timecnt/600));
				sec = String(Math.floor((timecnt%600)/10));
				msec = String(timecnt%10);
				if(sec.length == 1) {
					sec = "0" + sec;
				}
				$('#time')
					.text("{0}:{1}.{2}".format(min, sec, msec));
				if(timecnt == 32767) {
					clearInterval(id);
				}
			}, 100);
			mainexp();
			return false;
		})
});