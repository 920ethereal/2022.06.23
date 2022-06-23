<template>
	<view>
		<!--头像和会员名开始-->
		<view class="flex justify-between bg-white content1">
			<view class="flex">
				<view><image  class="user-logo" src="../../static/head.png"></image></view>
				<view style="margin-left: 20upx;">
					<view class="user-name">咸鱼用户</view>
					<view style="color: white;">2</view>
					<view>
						<text class="cu-tag bg-gradual-pink round">超级会员</text>
					</view>
				</view>
				
			</view>
			<view>
				
			</view>
			
		</view>
		<!--头像和会员名结束-->
		<!--订单开始-->
		<view class="flex justify-center">
			<view class="bg-white flex justify-around align-center" style="width: 700upx;height: 120upx;border-radius: 20upx;">
				<view style="position: relative;"class="flex align-center flex-direction"v-for="(p,i) in orders":key="i">
					<view :class="p.icon"style="font-size: 60upx">
					</view>
					<view style="position: absolute;top:0px;right: 0px;"class="cu-tag bg-red round sm">
					   {{p.num}}	
					</view>
			        <view>
						{{p.text}}
					</view>
				</view>
			</view>
		</view>
		<!--订单结束-->
		<!--列表开始-->
		<view style="margin-top: 10upx;">
			<!--每一个列表项-->
			<view @tap="gopage(i)"  class="bg-white list-item" v-for="(p,i) in lists" :key="i">
				<text>{{p.text}}</text>
			</view>
			<!--每一个列表项-->
			
		</view>
		<!--列表结束-->
		
	</view>
</template>

<script>
	export default {
		data() {
			return {
				orders:[
				{
					text:"待付款",
					icon:"cuIcon-pay",
					num:2,
					id:1
				},
				{
					text:"待分享",
					icon:"cuIcon-share",
					num:2,
					id:2
				},
				{
					text:"待发货",
					icon:"cuIcon-time",
					num:4,
					id:3
				},
				{
					text:"待收货",
					icon:"cuIcon-deliver",
					num:5,
					id:4
				},
				{
					text:"待评价",
					icon:"cuIcon-comment",
					num:2,
					id:5
				},
				],
				lists:[
					{
						text:"我的收藏"
					},
					{
						text:"退款售后"
					},
					{
						text:"收货地址"
					},
					{
						text:"在线客服"
					},
					{
						text:"系统设置"
					},
					{
						text:"注销登录",
						url:"../login/login"
					},
				]
		    }
		},
		methods: {
			gopage(item){
				var url=this.lists[item].url;
				if(url!=null&&url!=undefined){
					uni.reLaunch({
						url:url
					});
				}
				
			}
		}
	}
</script>

<style>
.user-logo{
	width: 150upx;
	height: 150upx;
}
.content1{
	padding: 30upx 30upx 30upx 200upx ;
	background-color: #FFFAE8;
	border-bottom: 5upx #FFA9C8 solid;
	border-top: 5upx #FFA9C8 solid;
	border-right: 5upx #FFA9C8 solid;
	border-left: 5upx #FFA9C8 solid;
}
.user-name{
	font-size: 120%;
	font-weight: bold;
}
.list-item{
	height: 80upx;
	display: flex;

	padding-left: 20upx;
	padding-right: 20upx;
	border-bottom: 2upx #FFFAE8 solid;
}
</style>
