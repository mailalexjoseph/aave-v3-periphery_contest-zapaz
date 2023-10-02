import "methods/Methods_base.spec";

///////////////// Properties ///////////////////////

// Certora prover bug, NOT a RewardController bug !
// Should not be able to set rewardOracle to 0
rule cannotSetRewardOracleWithoutPrice(method f, env e, calldataarg args) filtered {
   f -> !f.isView
}{
  address _rewardOracle = getRewardOracle(e, Reward);
  f(e, args);
  address rewardOracle_ = getRewardOracle(e, Reward);

  assert _rewardOracle != 0  => rewardOracle_ != 0 ;
}
