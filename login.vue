<template>
	<view>
		<!--logo设置-->
		<view style="margin-top: 200upx;" class="flex flex-direction align-center">
			<image class="user-logo" src="../../static/logo1.png"></image>
		</view>
		<!--logo设置-->
		<!--用户名和密码输入-->
		<view>
			<view class="input-fa">
				<input class="log-input" placeholder="用户名/邮箱/手机号"   v-model="form.phone" />
			</view>
			<view class="input-fa">
				<input class="log-input" placeholder="请输入密码" v-model="form.password" :password="true"/>
			</view>
		</view>
		<!--用户名和密码输入-->
		<!--登录按钮-->
		<view style="margin-top: 20upx;" class="justify-center">
			<button @tap="login" class="bg-gradual-pink round" style="width: 400upx;height: 100upx;">
				登录
			</button>
		</view>
		<!--登录按钮-->
		<!--忘记密码and新用户注册-->
		<view class="flex justify-between input-fa" style="margin-top: 20upx;">
			<text>忘记密码</text>
			<text>新用户注册</text>
		</view>
		<!--忘记密码and新用户注册-->
		<view style="position: fixed;bottom: 50upx;color:gray;text-align: center;width: 750upx;">
			登录代表您已同意【My Beauty商城隐私政策】
		</view>
		
	</view>
</template>

<script>
	export default {
		data() {
			return {
				form:{
					phone:"",
					password:""
				}
				
			}
		},
		methods: {
			changestatus(){
				this.status=this.status==0?1:0;
			},
			login(){
				uni.request({
					url:"http://172.17.99.170:4444/user/login",
					data:{
						phone:this.form.phone,
						password:this.form.password
					},
					method:"POST",
					success:(res)=>{
							uni.showToast({
									icon:"none",
									title:res.data.desc
								})
								console.log(res.data);
								if(res.data.status==0){
									uni.setStorageSync("uid",res.data.uid)
									uni.switchTab({
										url:"/pages/my/my"
									})
							}
					}
				})
			}
		}
	}
</script>

<style>
.user-logo{
	width: 200upx;
	height: 200upx;
}
.log-input{
	height: 100upx;
	border-bottom: 1upx solid #DDDDDD;
}
.input-fa{
	padding: 10upx 40upx 10upx 40upx;
}
</style>
