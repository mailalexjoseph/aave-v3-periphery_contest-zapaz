/////////////////////////////////////////////////////////////////////////////////
// Ensure reward if always in reward list (for ONE reward ONE asset)
/////////////////////////////////////////////////////////////////////////////////
rule rewardOneByAssetIsInList(method f, env e, calldataarg args) filtered {
    f -> !f.isView && !harnessFunction(f)
} {
  require rewardsOneAssetsOne(AToken, Reward);

  f@withrevert(e,args);

  address[] rewardsByAsset_ = getRewardsByAsset(AToken);
  address[] rewardsList_ = getRewardsList();

  assert rewardsByAsset_[0] == rewardsList_[0];
}

