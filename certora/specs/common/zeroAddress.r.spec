/////////////////////////////////////////////////////////////////////////////////
// Ensure asset balance cannot be changed
/////////////////////////////////////////////////////////////////////////////////
rule zeroAddressAssetUnchanged(method f, env e, calldataarg args) filtered {
   f -> !f.isView && !harnessFunction(f)
}{
  require e.msg.sender != 0;

  mathint _balance = AToken.balanceOf(e, 0);
  f@withrevert(e, args);
  mathint balance_ = AToken.balanceOf(e, 0);

  assert balance_ == _balance;
}

/////////////////////////////////////////////////////////////////////////////////
// Ensure reward of address zero cannot be changed
/////////////////////////////////////////////////////////////////////////////////
rule zeroAddressRewardUnchanged(method f, env e, calldataarg args) filtered {
   f -> !f.isView && !harnessFunction(f)
}{
  require e.msg.sender != 0;

  mathint _balance = Reward.balanceOf(e, 0);
  f@withrevert(e, args);
  mathint balance_ = Reward.balanceOf(e, 0);

  assert balance_ == _balance;
}

/////////////////////////////////////////////////////////////////////////////////
// Ensure transferStrategy cannot be set to zero
/////////////////////////////////////////////////////////////////////////////////
rule zeroAddressStrategyCannotBeSet(method f, env e, calldataarg args) filtered {
   f -> !f.isView && !harnessFunction(f)
}{
  address _transferStrategy = getTransferStrategy(Reward);
  f@withrevert(e, args);
  address transferStrategy_ = getTransferStrategy(Reward);

  assert _transferStrategy != 0 => transferStrategy_ != 0 ;
}
