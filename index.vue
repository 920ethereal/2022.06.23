<template>
       <view>
		   <view class="zhanwei"></view>
        <view class="cu-bar serach bg-gray">
			<view class="serach-form round">
				<input v-model="search" placeholder="请输入商品名"/>
				<!--设置搜索框-->
			</view>
			<view class="action">
				
			</view>
		</view>
		<view>
			<scroll-view class="nav bg-white " scroll-x>
				<view class="flex text-center ">
					<view  @click="qiehuan(index)" v-for="(item,index) in TabLists" :key="index" class="cu-item flex-sub" >
						{{item}}
					</view>
				</view>
			
			</scroll-view>
		</view>
		<!--轮播开始-->
		<swiper style="height: 250upx;" :circular="true" indicator-dots="true">
			<swiper-item>
				<image mode="scaleToFill" class="swiperimg" src="../../static/lan.jpg"></image><!--swiperimg设置轮播图高宽-->
			</swiper-item>
			<swiper-item>
				<image mode="scaleToFill" class="swiperimg" src="../../static/es.jpg"></image>
			</swiper-item>
			<swiper-item>
				<image mode="scaleToFill" class="swiperimg" src="../../static/bio.jpg"></image>
			</swiper-item>>
		</swiper>
		<!--轮播结束-->
		<!--特价开始-->
		  <!--特价标签开始-->
		<view class="tejia bg-white">
			<view class="flex align-center justify-between tejiabar">
				<view class="flex align-center">
				<view><image style="width: 100upx;height: 100upx;" src="../../static/sale.png"></image></view>
				<view style="font-size: 140%;" class="text-bold">清仓特价</view>
			</view>
			<view class="text-gray">
				查看全部<text class="cuIcon-right"></text>
			</view> 
	   </view>
	   <!--特价标签结束-->
	   <!--特价商品图片列表开始 iamge1定义图片长宽-->
	   <view class="flex">
			  <view>
				  <image class="image1" src="../../static/sale12345/sale1.jpg"></image>
			  </view>
			  <view>
			  	  <image class="image1" src="../../static/sale12345/sale2.jpg"></image>
			  </view>
			  <view>
			  	  <image class="image1" src="../../static/sale12345/sale3.jpg"></image>
			  </view>
			  <view>
			  	  <image class="image1" src="../../static/sale12345/sale4.jpg"></image>
			  </view>
			  <view>
			  	  <image class="image1" src="../../static/sale12345/sale5.jpg"></image>
			  </view>
	   </view>
	   <view class="flex justify-around" style="color: red">
		   <view>
			    ¥399
		   </view>
		   <view>
		   		¥299
		   </view>
		   <view>
		   	    ¥199
		   </view>
		   <view>
		   		¥599
		   </view>
		   <view>
		   		¥299
		   </view>
	   </view>
	   <!--特价商品图片列表结束-->
	   <!--商品推荐,image2定义推荐图片的格式-->
	   <view style="margin-top: 20upx;">
		    <view class="flex">
			   <image style="width: 300upx;height: 300upx;" src="../../static/reco/reco1.jpg"></image>
				   <view style="font-weight: 600;font-size:110%" >
					   <text class="cu-tag bg-gradual-pink round">特别推荐</text>
					    <view>Aussie 袋鼠蓬松洗发水</view>
						<view style="color: white;">2</view>
						<view style="color: white;">2</view>
						<view style="color: white;">2</view>
					    <view style="color: mediumvioletred;font-size: 125%;">¥35.00</view>
				   </view>
		    </view>
		    <view class="flex ">
			   <image style="width: 300upx;height: 300upx;" src="../../static/reco/reco2.jpg"></image>
			   <view style="font-weight: 600;font-size:110%">
				   <text class="cu-tag bg-gradual-pink round">特别推荐</text>
				   <view>YSL 圣罗兰黑丝缎凝露</view> 
				   <view style="color: white;">2</view>
				   <view style="color: white;">2</view>
				   <view style="color: white;">2</view>
				   <view style="color: mediumvioletred;font-size: 125%;">¥299.00</view>
				   
			   </view>
		    </view>
		    <view class="flex">
			   <image style="width: 300upx;height: 300upx;" src="../../static/reco/reco3.jpg"></image>
			   <view style="font-weight: 600;font-size:110%">
				   <text class="cu-tag bg-gradual-pink round">特别推荐</text>
				   <view>Givenchy 纪梵希心无禁忌香水</view>
				   <view style="color: white;">2</view>
				   <view style="color: white;">2</view>
				   <view style="color: white;">2</view>
				   <view style="color: mediumvioletred;font-size: 125%;">¥299.00</view>
			   </view>
		    </view>
		    <view class="flex">
			   <image style="width: 300upx;height: 300upx;" src="../../static/reco/reco4.jpg"></image>
			   <view style="font-weight: 600;font-size:110%">
				   <text class="cu-tag bg-gradual-pink round">特别推荐</text>
				   <view>Murad 慕拉德视黄醇面部精华</view>
				   <view style="color: white;">2</view>
				   <view style="color: white;">2</view>
				   <view style="color: white;">2</view>
				   <view style="color: mediumvioletred;font-size: 125%;">¥350.00</view>
				   
			   </view>
			</view>

		   
	   </view>
	   <!--商品推荐结束-->
	   
		</view>
       </view>
</template>

<script>
	export default {
		data() {
			return {
				shu:null,
				search:"",
				TabLists:["香水","洗护","护肤","彩妆","套装"],
				thistab:0,
				banners:[]
			}
		},
		onLoad() {
          this.getbanners();
		},
		methods: {
            qiehuan(index){
				this.thistab=index;
			},
			//获得轮播图的数据
			getbanners(){
				var data=[{
					url:"../../static/lan.jpg",
					action:" "
				},{
					url:"../../static/es.jpg",
					action:" "
				}];
				this.banners=data;
			}
		}
	}
</script>

<style>
	.content {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}

	.logo {
		height: 200rpx;
		width: 200rpx;
		margin-top: 200rpx;
		margin-left: auto;
		margin-right: auto;
		margin-bottom: 50rpx;
	}

	.text-area {
		display: flex;
		justify-content: center;
	}
  
	.title {
		font-size: 36rpx;
		color: #8f8f94;
	}
	.swiperimg{
		width: 750upx;
		height: 250upx;
	}
	.tejia{
		margin-top: 20upx;
	}
	.tejiabar{
		padding-left: 20upx;
		padding-right: 20upx;
	}
	.image1{
		width: 145upx;
		height: 145upx;
	}
	.zhanwei{
		height: var(--status-bar-height);
		weight:100% ;
	}

     
</style>
