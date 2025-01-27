from django.db import models

# Create your models here.
class TrafficLog(models.Model):
    flow_id = models.CharField(max_length=250)
    src_ip = models.CharField(max_length=250)
    src_port = models.IntegerField()
    dst_ip = models.CharField(max_length=250)
    dst_port = models.IntegerField()
    protocol = models.IntegerField()
    timestamp = models.CharField(max_length=100)
    flow_duration = models.FloatField()
    tot_fwd_pkts = models.FloatField()
    tot_bwd_pkts = models.FloatField()
    totlen_fwd_pkts = models.FloatField()
    totlen_bwd_pkts = models.FloatField()
    fwd_pkt_len_max = models.FloatField()
    fwd_pkt_len_min = models.FloatField()
    fwd_pkt_len_mean = models.FloatField()
    fwd_pkt_len_std = models.FloatField()
    bwd_pkt_len_max = models.FloatField()
    bwd_pkt_len_min = models.FloatField()
    bwd_pkt_len_mean = models.FloatField()
    bwd_pkt_len_std = models.FloatField()
    flow_byts_per_s = models.FloatField()
    flow_pkts_per_s = models.FloatField()
    flow_iat_mean = models.FloatField()
    flow_iat_std = models.FloatField()
    flow_iat_max = models.FloatField()
    flow_iat_min = models.FloatField()
    fwd_iat_tot = models.FloatField()
    fwd_iat_mean = models.FloatField()
    fwd_iat_std = models.FloatField()
    fwd_iat_max = models.FloatField()
    fwd_iat_min = models.FloatField()
    bwd_iat_tot = models.FloatField()
    bwd_iat_mean = models.FloatField()
    bwd_iat_std = models.FloatField()
    bwd_iat_max = models.FloatField()
    bwd_iat_min = models.FloatField()
    fwd_psh_flags = models.FloatField()
    bwd_psh_flags = models.FloatField()
    fwd_urg_flags = models.FloatField()
    bwd_urg_flags = models.FloatField()
    fwd_header_len = models.FloatField()
    bwd_header_len = models.FloatField()
    fwd_pkts_per_s = models.FloatField()
    bwd_pkts_per_s = models.FloatField()
    pkt_len_min = models.FloatField()
    pkt_len_max = models.FloatField()
    pkt_len_mean = models.FloatField()
    pkt_len_std = models.FloatField()
    pkt_len_var = models.FloatField()
    fin_flag_cnt = models.FloatField()
    syn_flag_cnt = models.FloatField()
    rst_flag_cnt = models.FloatField()
    psh_flag_cnt = models.FloatField()
    ack_flag_cnt = models.FloatField()
    urg_flag_cnt = models.FloatField()
    cwe_flag_count = models.FloatField()
    ece_flag_cnt = models.FloatField()
    down_per_up_ratio = models.FloatField()
    pkt_size_avg = models.FloatField()
    fwd_seg_size_avg = models.FloatField()
    bwd_seg_size_avg = models.FloatField()
    fwd_byts_per_b_avg = models.FloatField()
    fwd_pkts_per_b_avg = models.FloatField()
    fwd_blk_rate_avg = models.FloatField()
    bwd_byts_per_b_avg = models.FloatField()
    bwd_pkts_per_b_avg = models.FloatField()
    bwd_blk_rate_avg = models.FloatField()
    subflow_fwd_pkts = models.FloatField()
    subflow_fwd_byts = models.FloatField()
    subflow_bwd_pkts = models.FloatField()
    subflow_bwd_byts = models.FloatField()
    init_fwd_win_byts = models.FloatField()
    init_bwd_win_byts = models.FloatField()
    fwd_act_data_pkts = models.FloatField()
    fwd_seg_size_min = models.FloatField()
    active_mean = models.FloatField()
    active_std = models.FloatField()
    active_max = models.FloatField()
    active_min = models.FloatField()
    idle_mean = models.FloatField()
    idle_std = models.FloatField()
    idle_max = models.FloatField()
    idle_min = models.FloatField()
    label = models.CharField(max_length=100)
    sublabel = models.CharField(max_length=100,null=True)
