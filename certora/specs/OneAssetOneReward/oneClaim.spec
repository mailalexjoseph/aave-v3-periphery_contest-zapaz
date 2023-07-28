definition min(uint256 a, uint256 b) returns uint256 = ( a <= b ? a : b );
definition max(uint256 a, uint256 b) returns uint256 = ( a >= b ? a : b );

rule oneClaimAllRewardsAsExpected(env e, address user, address to) {
    require oneAssetOneReward(AToken, Reward);
    require e.msg.sender == user;
    require getTransferStrategy(Reward) != to;

    uint256 _amount = getUserRewards(e, getAssetsList(), user, Reward);
    uint256 _balance = Reward.balanceOf(e, to);
    uint256 _balancePlusAmount = require_uint256(_balance + _amount);

    address[] rewards_; uint256[] amounts_;
    rewards_, amounts_ = claimAllRewards(e, getAssetsList(), to);

    uint256 accrued = getUserAccruedRewards(user, Reward);
    assert accrued == 0;

    uint256 balance_ = Reward.balanceOf(e, to);
    assert balance_ == _balancePlusAmount;

    assert rewards_[0] == Reward;
    assert amounts_[0] == _amount;
}

rule oneClaimAllRewardsToSelfAsExpected(env e, address user) {
    require oneAssetOneReward(AToken, Reward);
    require e.msg.sender == user;
    require getTransferStrategy(Reward) != user;

    uint256 _amount = getUserRewards(e, getAssetsList(), user, Reward);
    uint256 _balance = Reward.balanceOf(e, user);
    uint256 _balancePlusAmount = require_uint256(_balance + _amount);

    address[] rewards_; uint256[] amounts_;
    rewards_, amounts_ = claimAllRewardsToSelf(e, getAssetsList());

    uint256 accrued = getUserAccruedRewards(user, Reward);
    assert accrued == 0;

    uint256 balance_ = Reward.balanceOf(e, user);
    assert balance_ == _balancePlusAmount;

    assert rewards_[0] == Reward;
    assert amounts_[0] == _amount;
}

rule oneClaimAllRewardsOnBehalfAsExpected(env e, address user, address to) {
    require oneAssetOneReward(AToken, Reward);
    require e.msg.sender == getClaimer(user);
    require getTransferStrategy(Reward) != to;

    uint256 _amount = getUserRewards(e, getAssetsList(), user, Reward);
    uint256 _balance = Reward.balanceOf(e, to);
    uint256 _balancePlusAmount = require_uint256(_balance + _amount);

    address[] rewards_; uint256[] amounts_;
    rewards_, amounts_ = claimAllRewardsOnBehalf(e, getAssetsList(), user, to);

    uint256 accrued = getUserAccruedRewards(user, Reward);
    assert accrued == 0;

    uint256 balance_ = Reward.balanceOf(e, to);
    assert balance_ == _balancePlusAmount;

    assert rewards_[0] == Reward;
    assert amounts_[0] == _amount;
}

rule oneClaimRewardsAsExpected(env e, address user, address to) {
    require oneAssetOneReward(AToken, Reward);
    require e.msg.sender == user;
    require getTransferStrategy(Reward) != to;

    uint256 amount;

    uint256 _amount = getUserRewards(e, getAssetsList(), user, Reward);
    uint256 _balance = Reward.balanceOf(e, to);
    uint256 _balancePlusAmount = require_uint256(_balance + min( _amount, amount ));

    uint256 amount_ = claimRewards(e, getAssetsList(), amount, to, Reward);

    uint256 balance_ = Reward.balanceOf(e, to);
    assert balance_ == _balancePlusAmount;

    assert amount_ == min( _amount, amount );
}

rule oneClaimRewardsOnBehalfAsExpected(env e, address user, address to) {
    require oneAssetOneReward(AToken, Reward);
    require e.msg.sender == getClaimer(user);
    require getTransferStrategy(Reward) != to;

    uint256 amount;
    uint256 _amount = getUserRewards(e, getAssetsList(), user, Reward);
    uint256 _balance = Reward.balanceOf(e, to);
    uint256 _balancePlusAmount = require_uint256(_balance + min( _amount, amount ));

    uint256 amount_ = claimRewardsOnBehalf(e, getAssetsList(), amount, user, to, Reward);

    uint256 balance_ = Reward.balanceOf(e, to);
    assert balance_ == _balancePlusAmount;

    assert amount_ == min( _amount, amount );
}

rule oneClaimRewardsToSelfAsExpected(env e, address user) {
    require oneAssetOneReward(AToken, Reward);
    require e.msg.sender == user;
    require getTransferStrategy(Reward) != user;

    uint256 amount;

    uint256 _amount = getUserRewards(e, getAssetsList(), user, Reward);
    uint256 _balance = Reward.balanceOf(e, user);
    uint256 _balancePlusAmount = require_uint256(_balance + min( _amount, amount ));

    uint256 amount_ = claimRewardsToSelf(e, getAssetsList(), amount, Reward);

    uint256 balance_ = Reward.balanceOf(e, user);
    assert balance_ == _balancePlusAmount;

    assert amount_ == min( _amount, amount );
}

