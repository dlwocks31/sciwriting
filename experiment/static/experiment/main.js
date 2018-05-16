String.prototype.format = function() {
  a = this;
  for (k in arguments) {
    a = a.replace("{" + k + "}", arguments[k])
  }
  return a
}
let ans, choices;
data = {'mode':0,'questions':[],'answeredTime':[],'iscorrect':[]};
hastime = true;
timecnt = 0;
MAXQCNT = 20
currqcnt = 0
hasquestion = false;
var timer;
function genchoice(i1, i2) {
	correctAt = Math.floor(Math.random() * 4)
	ret = [0,0,0,0];
	selected = [false,false,false,false,false,false,false,false];
	for(i=0;i<4;i++) {
		if(correctAt == i) {
			ret[i] = i1*i2;
			continue;
		}
		t = Math.floor(Math.random()*8);
		while(selected[t] || (i1*i2-10<=0 && t == 7))
			t = Math.floor(Math.random()*8);
		selected[t] = true;
		if(t == 0)
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
			ret[i] = i1*i2+10;
		else if(t == 7)
			ret[i] = i1*i2-10;
	}
	str = 'selected choice:'
	for(i=0;i<8;i++) {
		if(selected[i])
			str=str+i+' ';
	}
	console.log(str);
	return ret;
}

function putquestion() {
	i1 = Math.round(Math.random()*11+4);
	i2 = Math.round(Math.random()*11+4);
	ans = i1 * i2;
	choices = genchoice(i1, i2);
	data['questions'].push("{0} {1}".format(i1, i2));
	$('#question')
		.text("{0}×{1}=??".format(i1, i2));
	for(j=0; j<4; j++)
		$('#btn'+ (j+1)).text(choices[j]);
	hasquestion = true;
	console.log('hasquestion set to true');
}

function btnclick(i) {
	if(!hasquestion)
		return false;
	hasquestion = false;
	console.log('hasquestion set to false');
	if(ans == choices[i-1]) {
		data['iscorrect'].push(1);
		$('#btn'+i)
			.removeClass('btn-light')
			.addClass('btn-success');
		setTimeout(function() {
			$('#btn'+i)
				.removeClass('btn-success')
				.addClass('btn-light');
		}, 100);
	} else {
		data['iscorrect'].push(0);
		$('#btn'+i)
			.removeClass('btn-light')
			.addClass('btn-danger');
		setTimeout(function() {
			$('#btn'+i)
				.removeClass('btn-danger')
				.addClass('btn-light');
		}, 100);
	}
	data['answeredTime'].push(timecnt);
	currqcnt++;
	$('#remainq')
		.text(currqcnt + '/' + MAXQCNT);
	if(MAXQCNT == currqcnt)
		experimentend();
	else
		setTimeout(putquestion, 100);
	
}
function experimentend() {
	clearInterval(timer);
	$('#infotext')
		.text('실험이 종료되었습니다! 잠시 후 자동으로 다음 화면으로 넘어갑니다.');
	$('.exprow')
		.fadeOut(2000);
	$('#maindata')
		.val(JSON.stringify(data));
	setTimeout(function() {
		$('#mainform').submit();	
	}, 2500);		
}


$( document )
	.ready( function() {
		if($('#time').length) {
			data['mode'] = 'hastime';
			hastime = true;
		}
		else {
			data['mode'] = 'notime';
			hastime = false;
		}
		$('input[type=checkbox]').prop('checked', false);
		$('#mainbtn').click(function() {
			$('.exprow')
				.removeClass('hide');
			$('#infotext')
				.text('실험이 진행중입니다.')
			$('#remainq')
				.text('0/'+MAXQCNT);
			$(this)
				.text('실험 종료')
				.off('click')
				.addClass('hide');
			timer = setInterval(function() {
				timecnt++;
				if(hastime) {
					min = String(Math.floor(timecnt/600));
					sec = String(Math.floor((timecnt%600)/10));
					msec = String(timecnt%10);
					if(sec.length == 1) {
						sec = "0" + sec;
					}
					$('#time')
						.text("{0}:{1}.{2}".format(min, sec, msec));					
				}
				if(timecnt == 32767) {
					clearInterval(timer);
				}
			}, 100);				
			putquestion();
			return false;
		});
		$('#reportchk').change(function() {
			if(this.checked) {
				$('#emaildiv').removeClass('hide');
			} else {
				$('#emaildiv').addClass('hide');
			}
		});
		$('#lottochk').change(function() {
			if(this.checked) {
				$('#phonediv').removeClass('hide');
			} else {
				$('#phonediv').addClass('hide');
			}
		});
});

