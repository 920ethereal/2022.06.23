<template>
	<!--设置类目栏开始-->
	<view class="flex">
		<scroll-view scroll-y style="height: calc(100vh - 130upx);width: 200upx;">
			<view @tap="select(i)" :style="{fontSize:selected==i?'120%':'100%'}" :class="selected==i?'bg-white text bold':''"class="type-item" v-for="(p,i) in types":key="i">
				{{p}}
			</view>
		</scroll-view>
		<scroll-view scroll-with-animation :scroll-into-view="'good-'+selected" class="bg-white"scroll-y style="height: calc(100vh - 130upx);width: 550upx;">
			<view :id="'good-'+i"v-for="(p,i) in  goods" :key="i">
				<view>{{types[i]}}</view>
				<view class="flex flex-wrap">
					<view  class="flex justify-center align-center"style="width: 275upx;"v-for="(tp,ti) in p" :key="ti">

						<image style="width: 250upx;height: 250upx;":src="tp.url"></image>
						<!--<view style="text-align: center;">{{tp.name}}</view>
						<!--<view>{{tp.price}}</view>-->
					</view>
				</view>
				
			</view>
		</scroll-view>
		</view>
	</view>
	<!--设置类目栏结束-->
</template>

<script>
	export default {
		data() {
			return {
				search:"",
				types:[],
				goods:[],
				selected:0
			}
		},
		methods: {
			gettypes(){
				var data=[]

				    data.push("香水")
					data.push("洗护")
					data.push("护肤")
					data.push("彩妆")
					data.push("套装")
			this.types=data;
			
		 },
		 getgoods(){
			 var data=[];
			 for(var i=0;i<6;i++){
				 var p=[];
				 if(i==0){
				 p.push({url:"../../static/static1/1c.jpg",name:this.types[i]+i,price:i*2});
				 p.push({url:"../../static/static1/1g.jpg",name:this.types[i]+i,price:i*2});
			 	 p.push({url:"../../static/static1/1p.jpg",name:this.types[i]+i,price:i*2});
				 }
			    if(i==1){
			    p.push({url:"../../static/static1/2a.jpg",name:this.types[i]+i,price:i*2});
			    p.push({url:"../../static/static1/2b.jpg",name:this.types[i]+i,price:i*2});
			    p.push({url:"../../static/static1/2k.jpg",name:this.types[i]+i,price:i*2});
			    }
				if(i==2){
				p.push({url:"../../static/static1/3l.jpg",name:this.types[i]+i,price:i*2});
				p.push({url:"../../static/static1/3m.jpg",name:this.types[i]+i,price:i*2});
				p.push({url:"../../static/static1/3y.jpg",name:this.types[i]+i,price:i*2});
				}
				if(i==3){
				p.push({url:"../../static/static1/4h.jpg",name:this.types[i]+i,price:i*2});
				p.push({url:"../../static/static1/4y.jpg",name:this.types[i]+i,price:i*2});
				p.push({url:"../../static/static1/4y2.jpg",name:this.types[i]+i,price:i*2});
				}
				if(i==4){
				p.push({url:"../../static/static1/5a.jpg",name:this.types[i]+i,price:i*2});
				p.push({url:"../../static/static1/5f.jpg",name:this.types[i]+i,price:i*2});
				p.push({url:"../../static/static1/5n.jpg",name:this.types[i]+i,price:i*2});
				}
				 data.push(p);
			 };

			 this.goods=data;
		 },
		 select(i){
			 this.selected=i;
		 }
		},
		onLoad() {
			this.gettypes();
			this.getgoods();
		}
}

</script>

<style>
.type-item{
	height: 200upx;
	text-align: center;
	line-height: 100upx;
}
</style>
