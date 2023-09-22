# Kill the killmenow process using pkill
exec { 'killmenow':
  command => 'pkill killmenow',
}
