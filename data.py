# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import time
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

m_file_path = "goods_demand_plan_file\\"
m_id_start = 13000000
m_data_count = 1000002
m_batch_num = 1000
m_main_header_id_base = 1500000002000000000
m_main_code_base = 1200000000
m_item_id_base = 1510000102000000000
m_tenant_extend_id_base = 1520000202000000000

m_insert_main_header = "INSERT INTO `mt_buyer_goods_demand_plan_info` (`id`, `buyer_tenant_id`, `supplier_tenant_id`, `address_id`, `batch_code`, `row_code`, `bom`, `safe_stock`, `buyer_order`, `buyer_order_row_code`, `buyer_org_id`, `buyer_org_code`, `buyer_org_name`, `warehouse_keeper`, `site_id`, `site_code`, `site_name`, `work_center`, `work_center_code`, `work_center_name`, `company_id`, `company_code`, `company_name`, `supplier_id`, `supplier_code`, `supplier_name`, `processor_id`, `processor_code`, `processor_name`, `plan_group_id`, `plan_group_code`, `plan_group_name`, `warehouse_id`, `warehouse_code`, `warehouse_name`, `warehouse_qty`, `delivery_method`, `supplier_check_user`, `check_date`, `item_id`, `item_code`, `item_name`, `item_description`, `system_remark`, `sale_order`, `sale_order_row_code`, `delivery_status`, `project_text_batch`, `product_code`, `process_name`, `associated_number`, `schedule_type`, `schedule_area`, `outsourced_type`, `released`, `serial_number`, `create_user_id`, `create_user_name`, `create_time`, `update_user_id`, `update_user_name`, `update_time`, `abolished`, `item_group_id`, `item_group_code`, `item_group_name`, `request_order_method`, `receipt_part_code`, `receipt_part_name`, `receive_address_code`, `receive_address_name`) VALUES "
m_insert_main_value = "({}, 10000, 1513441933864919041, 1504025649763848193, '', '', '', 0.00000000, '1100929157', '10', 0, '', '', '', 0, '1000', '冰箱生产工厂', '', '', '', 0, '0530', 'TCL家用电器（合肥）有限公司', 0, '100358', '启东市汇通螺丝厂', 0, '', '', 0, '', '', 0, 'Y003', '钣金材料仓', 0.00000000, '1', '', 0, 0, '4B120-000313', '冷冻门端盖/ABS/芭蕾白C103/上/118', '', '', '', '', 0, '', '', '', '', '', '', '', '', '0182138705000010', 0, 'system', 1649686956060, 0, '', 0, 0, 0, '', '  ', 0, '', '', 'BD-F-FPS-001', '53253253252')".encode("utf-8")

m_insert_item_header = "INSERT INTO `mt_buyer_goods_demand_plan_item_info` (`id`, `goods_demand_plan_id`, `tenant_id`, `type`, `time_info`, `time_info_timestamp`, `total`, `buyer_num`, `gap_num`, `supplier_num`, `status`, `old_status`, `buyer_remark`, `supplier_remark`, `released`, `jit`, `limit_num`, `outstanding_num`, `remaining_num`, `receive_num`, `delivery_num`, `goods_supply_plan`, `create_time`, `create_user_id`, `create_user_name`, `update_time`, `update_user_id`, `update_user_name`, `abolished`, `supplier_check_user`, `check_date`) VALUES "
m_insert_item_value = "({}, {}, 10000, '', '2022/04/11', 1649606400000, 1000000.00000000, 1000000.00000000, 0.00000000, 1000000.00000000, 5, 3, '', '', '0', 0, 0.00000000, 0.00000000, 989344.00000000, 10656.00000000, 0.00000000, 1, 1649686956119, 0, 'system', 1649925212011, 0, 'system', 0, '启东汇通', 1649692757647)".encode("utf-8")

m_insert_tenant_extend_header = "INSERT INTO `mt_site_tenant_extend` (`id`, `tenant_id`, `config_group_type`, `site_id`, `site_code`, `site_name`, `site_address`, `site_address_name`, `sub_site_code`, `sub_site_name`, `sub_site_address`, `sub_site_address_name`, `supplier_id`, `supplier_code`, `supplier_name`, `consignee_name`, `consignee_phone`, `consignee_address_code`, `consignee_address`, `status`, `need_default`, `relation_item_expend`, `create_user_id`, `create_user_name`, `create_time`, `update_user_id`, `update_user_name`, `update_time`, `abolished`) VALUES "
m_insert_tenant_extend_value = "({}, 10000, 1, 1486316872849100801, '1010', '惠州王牌内销制造中心', 'FGC20220126122345_返工仓', '', '', '', '', '', 0, '', '', '吴林健', '13813223211', '', '苏州市虎丘区科沃斯工厂', 0, 1, 0, 1490973294854447106, '顾涛', 1647402434730, 1490973294854447106, '租户管理员', 1647527688054, 1)".encode("utf-8")


# m_insert_order_sql = "INSERT INTO `mt_buyer_order` (`id`, `tenant_id`, `tenant_name`, `order_code`, `source`, `origin_source`, `business_type_id`, `business_type_code`, `business_type_name`, `status`, `publish_status`, `feedback_status`, `delivery_status`, `receive_status`, `warehouse_status`, `type`, `order_type_code`, `order_type_name`, `contract_type`, `allocation_mode`, `acceptance_use`, `payment_code`, `payment_name`, `free_total`, `tax_total`, `currency_id`, `currency_code`, `currency_name`, `project_type`, `project_id`, `project_code`, `project_name`, `supplier_id`, `supplier_code`, `supplier_name`, `supplier_add`, `company_id`, `company_code`, `company_name`, `buyer_user_id`, `buyer_user_code`, `buyer_user_name`, `buyer_org_id`, `buyer_org_code`, `buyer_org_name`, `buyer_group_id`, `buyer_group_code`, `buyer_group_name`, `settlement_id`, `settlement_name`, `invoice_id`, `required_delivery_date`, `remark`, `urgent_time`, `publish_time`, `publish_user_id`, `feedback_time`, `feedback_user_id`, `feedback_user`, `order_rel`, `other_data_pew`, `sup_remark`, `create_time`, `create_user_id`, `create_user_name`, `update_time`, `update_user_id`, `update_user_name`, `abolished`, `version`, `latest_version`, `after_sale_flag`, `process_instance_id`, `enterprise_code`, `enterprise_name`, `order_time`) VALUES ({}, 10000, 'TCL', '{}', 3, 3, 1493479350943789058, 'BTTCL004', '物资类', 2, 1, 2, 1, 1, 0, 0, 'T1', '内销标准采购订单', 0, 2, 0, 'HF01', '发票挂账3个月后,付6个月银行承兑汇票', 150000.0000, 150000.0000, 1512987130042712065, 'CNY', '中国人民币', 0, 0, '', '', 1335321443038992600, '100358', '启东市汇通螺丝厂', '', 1512620484903219202, '0530', 'TCL家用电器（合肥）有限公司', 0, '-1', '', 1512417655861194753, 'C03', '结构件', 1512621453690974209, 'HF00', 'TCL合肥内销采购组织', 0, '', 0, 0, '', 0, 1649988496543, 0, 1650267356894, 1513441922480390146, '启东汇通', '', '', '', 1649988496172, 0, 'system', 1650267356952, 1513441922480390146, '启东汇通', 0, 2, 1, 0, 0, '', '', 1649980800000);".encode("utf-8")
# m_insert_order_detal_sql1 = "INSERT INTO `mt_buyer_order_detail` (`id`, `tenant_id`, `order_id`, `order_code`, `item_no`, `item_id`, `item_code`, `item_name`, `item_group_code`, `item_group_name`, `category_id`, `category_code`, `category_name`, `sku_id`, `sku_code`, `sku_name`, `sku_pic_url`, `specification`, `unit_id`, `unit_code`, `unit_name`, `pur_unit_id`, `pur_unit_name`, `pur_unit_code`, `site_id`, `site_code`, `site_name`, `buyer_org_id`, `buyer_org_code`, `buyer_org_name`, `buyer_dep_id`, `buyer_dep_code`, `buyer_dep_name`, `delivery_status`, `pre_delivery_qty`, `delivery_qty`, `receive_status`, `pre_receive_qty`, `receive_qty`, `confirm_status`, `quantity`, `currency_id`, `currency_code`, `currency_name`, `free_price`, `tax_price`, `tax_code`, `taxid`, `free_total`, `tax_total`, `posting_account`, `trade_clause_id`, `trade_clause_code`, `trade_clause_name`, `shipping_method_code`, `shipping_method_name`, `receive_site_id`, `receive_site_code`, `receive_site_name`, `receive_address_id`, `receive_address`, `consignee_id`, `consignee`, `warehouse_status`, `warehouse_id`, `warehouse_code`, `warehouse`, `warehouse_qty`, `pre_warehouse_qty`, `contact_id`, `contact`, `quality_exemption_mark_id`, `quality_exemption_mark_code`, `quality_exemption_mark_name`, `package_method`, `package_spec`, `package_desc`, `product_code`, `product_name`, `check_request`, `remark`, `urgent_time`, `purchase_strategy`, `subject_type`, `project_name`, `project_code`, `project_text_batch`, `project_row_text`, `transit_qty`, `un_price`, `un_total`, `change_remark`, `other_data_pew`, `required_delivery_date`, `customer_order`, `customer_order_line_no`, `return_identification`, `create_time`, `create_user_id`, `create_user_name`, `update_time`, `update_user_id`, `update_user_name`, `abolished`, `version`, `latest_version`, `request_order_method`, `provisional_estimate_status`, `close_status`, `order_rel`, `asset_type`, `asset_card`, `asset_code`, `work_order_rel`, `price_unit`, `sup_remark`, `time_promise`, `customer_name`, `after_sale_flag`, `settled_status`) VALUES ({}, 10000, {}, '1100929216', 10, 0, '4B122-000204', '瓶托/GPPS/琥珀灰C214/无丝印/无烫银/上/118', '4B12201', '瓶托', 0, '', '', 0, '', '', '', '', 29306882, 'PC', '个', 1512624424969482241, '个', 'PC', 1512620485289095170, '1000', '冰箱生产工厂', 0, 'C03', '结构件', 0, '', '', 1, 9000.00000000, 1000.00000000, 1, 9001.00000000, 999.00000000, 2, 10000.00000000, 1512987130042712065, 'CNY', '中国人民币', 10.0000, 10.0000, '', 0.00000000, 100000.0000, 100000.0000, '', 0, '', '', '', '', 0, '', '', 0, '', 0, '', 0, 0, 'Y003', '钣金材料仓', 0.00000000, 0.00000000, 0, '', 0, '', '', '', '', '', '', '', '', '', 0, 0, 5, '', '', '', '', 1.00000000, -99.0000, -99.0000, '', '', 1650556800000, '', 0, 0, 1649988496387, 0, 'system', 1650267356976, 1513441922480390146, '启东汇通', 0, 2, 1, NULL, 0, 0, '', '', '', '', '', 1.0000, '', 1650556800000, '', NULL, 0);".encode("utf-8")
# m_insert_order_detal_sql2 = "INSERT INTO `mt_buyer_order_detail` (`id`, `tenant_id`, `order_id`, `order_code`, `item_no`, `item_id`, `item_code`, `item_name`, `item_group_code`, `item_group_name`, `category_id`, `category_code`, `category_name`, `sku_id`, `sku_code`, `sku_name`, `sku_pic_url`, `specification`, `unit_id`, `unit_code`, `unit_name`, `pur_unit_id`, `pur_unit_name`, `pur_unit_code`, `site_id`, `site_code`, `site_name`, `buyer_org_id`, `buyer_org_code`, `buyer_org_name`, `buyer_dep_id`, `buyer_dep_code`, `buyer_dep_name`, `delivery_status`, `pre_delivery_qty`, `delivery_qty`, `receive_status`, `pre_receive_qty`, `receive_qty`, `confirm_status`, `quantity`, `currency_id`, `currency_code`, `currency_name`, `free_price`, `tax_price`, `tax_code`, `taxid`, `free_total`, `tax_total`, `posting_account`, `trade_clause_id`, `trade_clause_code`, `trade_clause_name`, `shipping_method_code`, `shipping_method_name`, `receive_site_id`, `receive_site_code`, `receive_site_name`, `receive_address_id`, `receive_address`, `consignee_id`, `consignee`, `warehouse_status`, `warehouse_id`, `warehouse_code`, `warehouse`, `warehouse_qty`, `pre_warehouse_qty`, `contact_id`, `contact`, `quality_exemption_mark_id`, `quality_exemption_mark_code`, `quality_exemption_mark_name`, `package_method`, `package_spec`, `package_desc`, `product_code`, `product_name`, `check_request`, `remark`, `urgent_time`, `purchase_strategy`, `subject_type`, `project_name`, `project_code`, `project_text_batch`, `project_row_text`, `transit_qty`, `un_price`, `un_total`, `change_remark`, `other_data_pew`, `required_delivery_date`, `customer_order`, `customer_order_line_no`, `return_identification`, `create_time`, `create_user_id`, `create_user_name`, `update_time`, `update_user_id`, `update_user_name`, `abolished`, `version`, `latest_version`, `request_order_method`, `provisional_estimate_status`, `close_status`, `order_rel`, `asset_type`, `asset_card`, `asset_code`, `work_order_rel`, `price_unit`, `sup_remark`, `time_promise`, `customer_name`, `after_sale_flag`, `settled_status`) VALUES ({}, 10000, {}, '1100929216', 20, 0, '4B122-000204', '瓶托/GPPS/琥珀灰C214/无丝印/无烫银/上/118', '4B12201', '瓶托', 0, '', '', 0, '', '', '', '', 29306882, 'PC', '个', 1512624424969482241, '个', 'PC', 1512620485289095170, '1000', '冰箱生产工厂', 0, 'C03', '结构件', 0, '', '', 0, 5000.00000000, 0.00000000, 0, 0.00000000, 0.00000000, 2, 5000.00000000, 1512987130042712065, 'CNY', '中国人民币', 10.0000, 10.0000, '', 0.00000000, 50000.0000, 50000.0000, '', 0, '', '', '', '', 0, '', '', 0, '', 0, '', 0, 0, 'Y003', '钣金材料仓', 0.00000000, 0.00000000, 0, '', 0, '', '', '', '', '', '', '', '', '', 0, 0, 5, '', '', '', '', 0.00000000, -99.0000, -99.0000, '', '', 1650556800000, '', 0, 0, 1649988496406, 0, 'system', 1650267356988, 1513441922480390146, '启东汇通', 0, 2, 1, NULL, 0, 0, '', '', '', '', '', 1.0000, '', 1650556800000, '', NULL, 0);".encode("utf-8")
# m_insert_order_detal_require_sql1 = "INSERT INTO `mt_buyer_order_detail_require` (`id`, `tenant_id`, `order_id`, `order_detail_id`, `forecast_qty`, `purchasing_cycle_start`, `purchasing_cycle_end`, `required_delivery_date`, `contract_type`, `contract`, `contract_rel_id`, `contract_rel`, `contract_rel_code`, `budget_code`, `budget_unit_price`, `budget_total_price`, `budget_subject`, `subject_total`, `taxed_unit_price`, `taxed_total_price`, `approved_total_price`, `posting_account_id`, `posting_account_code`, `posting_account_name`, `require_name`, `requirement_description`, `profit_center_id`, `profit_center_code`, `profit_center_name`, `create_time`, `create_user_id`, `create_user_name`, `update_time`, `update_user_id`, `update_user_name`, `abolished`, `version`, `latest_version`, `art_param`, `tech_contact_person`) VALUES ({}, 10000, {}, {}, 0.00000000, 0, 0, 1650556800000, 0, '', 0, '', '', '', -99.0000, -99.0000, '', -99.0000, -99.0000, -99.0000, -99.0000, 0, '', '', '', '', 0, '', '', 1649988496399, 0, 'system', 0, 0, '', 0, 2, 1, '', '');"
# m_insert_order_detal_require_sql2 = "INSERT INTO `mt_buyer_order_detail_require` (`id`, `tenant_id`, `order_id`, `order_detail_id`, `forecast_qty`, `purchasing_cycle_start`, `purchasing_cycle_end`, `required_delivery_date`, `contract_type`, `contract`, `contract_rel_id`, `contract_rel`, `contract_rel_code`, `budget_code`, `budget_unit_price`, `budget_total_price`, `budget_subject`, `subject_total`, `taxed_unit_price`, `taxed_total_price`, `approved_total_price`, `posting_account_id`, `posting_account_code`, `posting_account_name`, `require_name`, `requirement_description`, `profit_center_id`, `profit_center_code`, `profit_center_name`, `create_time`, `create_user_id`, `create_user_name`, `update_time`, `update_user_id`, `update_user_name`, `abolished`, `version`, `latest_version`, `art_param`, `tech_contact_person`) VALUES ({}, 10000, {}, {}, 0.00000000, 0, 0, 1650556800000, 0, '', 0, '', '', '', -99.0000, -99.0000, '', -99.0000, -99.0000, -99.0000, -99.0000, 0, '', '', '', '', 0, '', '', 1649988496415, 0, 'system', 0, 0, '', 0, 2, 1, '', '');"

def start():
    data_id = m_main_header_id_base + m_id_start
    data_code = m_main_code_base + m_id_start
    data_item_id = m_item_id_base + m_id_start
    data_tenant_extend_id = m_tenant_extend_id_base + m_id_start
    
    # file = m_file_path + "mt_buyer_order_insert.sql"
    f_ordeMain = open(m_file_path + "mt_buyer_goods_demand_plan_info_insert_{}.sql".format(m_data_count),'ab')
    f_orderItem = open(m_file_path + "mt_buyer_goods_demand_plan_item_info_insert_{}.sql".format(m_data_count),'ab')
    f_tenant_extend = open(m_file_path + "mt_site_tenant_extend_insert_{}.sql".format(m_data_count),'ab')
    f_ordeMain.write(m_insert_main_header)
    f_ordeMain.write("\r\n")
    f_orderItem.write(m_insert_item_header)
    f_orderItem.write("\r\n")
    f_tenant_extend.write(m_insert_tenant_extend_header)
    f_tenant_extend.write("\r\n")
    
    # f.write(m_insert_order_sql.encode("utf-8"))
    for i in range(m_data_count):
        data_id += 1
        data_code += 1        
        data_item_id += 1
        data_tenant_extend_id += 1
        sql_main = m_insert_main_value.format(data_id)
        sql_item = m_insert_item_value.format(data_item_id,data_id)
        sql_tenant_extend = m_insert_tenant_extend_value.format(data_tenant_extend_id)
        
        # if i < m_data_count-1: flag = ","
        # else: flag = ";"
        
        if (i+1) % m_batch_num == 0 :
            flag = ";"
        else:
            flag = ","

        f_ordeMain.write(sql_main)
        f_ordeMain.write(flag)
        f_ordeMain.write("\r\n")
        
        f_orderItem.write(sql_item)
        f_orderItem.write(flag)
        f_orderItem.write("\r\n")
        
        f_tenant_extend.write(sql_tenant_extend)
        f_tenant_extend.write(flag)
        f_tenant_extend.write("\r\n")
        
        if flag == ";" and (i+1) < m_data_count:
            f_ordeMain.write(m_insert_main_header)
            f_ordeMain.write("\r\n")
            f_orderItem.write(m_insert_item_header)
            f_orderItem.write("\r\n")
            f_tenant_extend.write(m_insert_tenant_extend_header)
            f_tenant_extend.write("\r\n")
        
    f_ordeMain.close()
    f_orderItem.close()
    f_tenant_extend.close()
        
    # print m_file_path
    
    
start()
