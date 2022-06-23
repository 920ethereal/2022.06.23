<template>
	
	<view>
		<!--设置全选和删除 开始-->
		<view class="caozuo">
			<view>
				<checkbox-group @change="changeAll">
				<checkbox :checked="checked" :class="checked==true?'checked':''"  class="round sx-check">
				</checkbox>
				<text>全选</text>
				</checkbox-group>
			</view>
			<view>
				<view class="cu-btn sm round"><text class="cuIcon-delete"></text>删除</view>
			</view>
		</view>
		<!--设置全选和删除 结束-->
		<!--设置购物车商品 开始-->
		<view class="cart-content">
			<view v-for="(p,i) in lists" :key="i" class="cart-item bg-white">
				<view class="flex align-center">
					<checkbox-group>
					<checkbox :checked="p.checked" :class="p.checked==true?'checked':''"  class="round sx-check"></checkbox>
					</checkbox-group>
					<image :src="p.img"></image>
				</view>
				<view style="width: 450upx;">
					<view class="cart-title">{{p.title}}</view>
					<view>
						<view class="text-gray">{{p.type}}</view>
						<view>
							<view style="font-size: 120%;"class="text-red text-bold text-lg">¥{{p.price}}</view>
							<uni-number-box :itemIndex="i" @change="changejishu":v-model="p.num" :min="0" :max="9"></uni-number-box>
						</view>
					</view>
				</view>
			</view>
		</view>
		<!--设置购物车商品 结束-->
		<!--设计合计和结算 开始-->
		<view class="heji flex justify-between align-center">
			<view style="font-size: 115%;">合计<text class="text-orange">{{sum}}</text></view>
			<view>
				<button @tap="tijiao" class="cu-btn bg-gradual-pink round ">
								结算
				</button>
			</view>
			
		</view>
		<!--设置合计和结算 结束-->
	</view>
	
</template>

<script>
	import uniNumberBox from"@/uni_modules/uni-number-box/components/uni-number-box/uni-number-box.vue"
	export default {
		data() {
			return {
				checked:true,
                lists:[]
			}
		},
		onLoad() {
			this.getdata();
		},
		//定义计算属性
		computed:{
			sum(){
				var he=0;
				console.log(this.lists.length);
				this.lists.forEach(p=>{
					if(p.checked==true){
						console.log(p.num);
						he+=p.num*p.price;
					}
				});
				console.log("总价-------");
				console.log(he);
				return he;
			} 
			
		},
		components: {
			uniNumberBox
		},
		methods: {
			tijiao(){
				uni.showModal({
				    title: '提示',
				    content: '您确定要提交订单吗？',
				    success: function (res) {
				        if (res.confirm) {
				            uni.showToast({
				                title: '提交成功',
				                duration: 2000
				            });

				        } 
				    }
				});

			},
			changejishu(itemIndex,val){
				val=parseInt(val);
				this.lists[itemIndex].num = val;
				if(val==0){
					var thisdata=this.lists.find(p=>{
						return p.num==0;
					})
					//数量为0时提示是否删除商品
					uni.showModal({
						confirmText:"是的",
						content:"确定要从购物车删除这个商品吗？",
						title:"删除警告",
						success() {
						}
					})
				}
			},
			changeAll(e){
				this.checked?this.checked=false:this.checked=true;
			},
			getdata(){
				var data=[{
					id:1,
					img:"../../static/sale12345/sale4.jpg",
					title:"潘海利根luna月亮女神香水",
					type:"30ml",
					price:399.00,
					num:1,
					checked:true
				},{
					id:1,
					img:"../../static/sale12345/sale3.jpg",
					title:"卡诗钥源黑钻鱼子酱发膜",
					type:"200ml",
					price:260.00,
					num:1,
					checked:true
				},{
					id:1,
					img:"../../static/sale12345/sale2.jpg",
					title:"雅诗兰黛微精华樱花水",
					type:"200ml",
					price:399.00,
					num:1,
					checked:true
				}];
				this.lists=data;
			}
		}
	}
</script>

<style>
.sx-check{
	transform: scale(0.7);
}
.caozuo{
	position: fixed;
	top: 110upx;
	background-color: white;
	display: flex;
	justify-content: space-between;
	height: 80upx;
	align-items: center;
	width: 750upx;
	padding-left: 30upx;
	padding-right:30upx ;
}
.cart-content{
	margin-top: 80upx;
	margin-bottom: 200upx;
	
}
.cart-item{
	display: flex;
	justify-content: space-between;
	padding: 30upx 30upx 30upx 30upx;
	margin-top: 20upx;
}
.cart-item image{
	width: 200upx;
	height: 200upx;
}
.cart-title{
	font-size: 110%;
	font-weight: bold;
	overflow: hidden;
	text-overflow: ellipsis;
	white-space: nowrap;
}
.heji{
	position: fixed;
	bottom: 100upx;
	width: 750upx;
	height: 100upx;
	background-color: pink;
	padding-right: 30upx;
	padding-left: 30upx;
}


</style>
