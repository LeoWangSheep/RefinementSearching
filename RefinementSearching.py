# The hierarchy set, some goals might have hierarchy state
h_set = {1: {'state': [
            {'current': ['allocate_s'], 'next': [], 'always': ['in_p_sys'], 'eventually': [],
             'untilbefore': [], 'untilafter': []},
        ]},
        2: {'state': [
            {'current': [], 'next': [], 'always': ['in_p_sys'], 'eventually': [],
             'untilbefore': [], 'untilafter': []},
        ]},
        3: {'state': [
            {'current': ['monitored_u_s'], 'next': [], 'always': [], 'eventually': ['reported_s'],
             'untilbefore': [], 'untilafter': []},
        ]},
        4: {'state': [
            {'current': [], 'next': [], 'always': ['in_p_sys'], 'eventually': [],
             'untilbefore': [], 'untilafter': []},
        ]},
        5: {'state': [
            {'current': ['monitored_u_s'], 'next': [], 'always': [], 'eventually': ['in_mn_sys'],
             'untilbefore': [], 'untilafter': []},
            {'current': ['monitored_u_s'], 'next': [], 'always': [], 'eventually': ['in_me_sys'],
             'untilbefore': [], 'untilafter': []},
        ]},
        6: {'state': [
            {'current': ['in_me_sys'], 'next': [], 'always': [], 'eventually': [],
             'untilbefore': ['in_me_sys'], 'untilafter': ['reported_s']},
        ]},
    }

# Every goal will be represented as a dictionary which includes id, name, and all possible states
# this goal will be.  This data structure like a formatted representation of every goal.
goal_set = [{'goal_id': 1, 'state': [
                {'current': ['receive_srv_sys'], 'next': [], 'always': ['monitored_u_s'], 'eventually': [h_set[1]],
                 'untilbefore': [], 'untilafter': []},
            ], 'name': 'ConnectToUniversity'},
            {'goal_id': 2, 'state': [
                {'current': ['created_u_p_sys'], 'next': [], 'always': [], 'eventually': [h_set[2]],
                 'untilbefore': [], 'untilafter': []},
            ], 'name': 'ProjectRegister'},
            {'goal_id': 3, 'state': [
                {'current': ['invited_a_p', 'in_p_sys'], 'next': [], 'always': [],
                 'eventually': ['allocate_s', 'exported_s'], 'untilbefore': [], 'untilafter': []},
            ], 'name': 'ProjectManagement'},
            {'goal_id': 4, 'state': [
                {'current': [], 'next': [], 'always': [h_set[3]], 'eventually': [], 'untilbefore': [], 'untilafter': []},
            ], 'name': 'StudentMonitor'},
            {'goal_id': 5, 'state': [
                {'current': ['created_u_p_sys'], 'next': [], 'always': [], 'eventually': ['in_st_sys'],
                 'untilbefore': [], 'untilafter': []},
            ], 'name': 'StudentTableImport'},
            {'goal_id': 6, 'state': [
                {'current': ['created_u_p_sys'], 'next': [], 'always': [], 'eventually': ['in_pi_p'],
                 'untilbefore': [], 'untilafter': []},
            ], 'name': 'ProjectInfoInput'},
            {'goal_id': 7, 'state': [
                {'current': ['in_st_sys'], 'next': [], 'always': [], 'eventually': ['selected_s'],
                 'untilbefore': [], 'untilafter': []},
            ], 'name': 'TargetStudentSelection'},
            {'goal_id': 8, 'state': [
                {'current': ['in_pi_p', 'selected_s'], 'next': [], 'always': [], 'eventually': [h_set[4]],
                 'untilbefore': [], 'untilafter': []},
            ], 'name': 'RepositeProject'},
            {'goal_id': 9, 'state': [
                {'current': ['in_p_sys', 'received_st_sys'], 'next': [], 'always': [],
                 'eventually': ['exported_s'], 'untilbefore': [], 'untilafter': []},
            ], 'name': 'StudentInfoExport'},
            {'goal_id': 10, 'state': [
                {'current': ['invited_a_p'], 'next': [], 'always': [], 'eventually': ['allocate_s'],
                 'untilbefore': [], 'untilafter': []},
            ], 'name': 'StudentAllocation'},
            {'goal_id': 11, 'state': [
                {'current': ['invited_a_p', 'not_known_a'], 'next': [], 'always': [], 'eventually': ['known_a'],
                 'untilbefore': [], 'untilafter': []},
            ], 'name': 'ReplyNotification'},
            {'goal_id': 12, 'state': [
                {'current': ['invited_a_p', 'known_a'], 'next': [], 'always': [], 'eventually': ['allocate_s'],
                 'untilbefore': [], 'untilafter': []},
            ], 'name': 'ReplyAllocation'},
            {'goal_id': 13, 'state': [
                {'current': [], 'next': [], 'always': [h_set[5]], 'eventually': [], 'untilbefore': [], 'untilafter': []},
            ], 'name': 'MonitorResultGeneration'},
            {'goal_id': 14, 'state': [
                {'current': [], 'next': [], 'always': [h_set[6]], 'eventually': [], 'untilbefore': [], 'untilafter': []},
            ], 'name': 'ExceptionMessageReport'},
            ]

# The milestone is the predicate that can help finish one task from one state to
# another state. The milestone can help us mine potential hierarchy relationship
milestones = {'in_st_sys': {'from': {'predicate': 'created_u_p_sys', 'type': 'current'},
                            'to': {'predicate': 'in_p_sys', 'type': 'always'}},
              'in_pi_p': {'from': {'predicate': 'created_u_p_sys', 'type': 'current'},
                          'to': {'predicate': 'in_p_sys', 'type': 'always'}},
              'selected_s': {'from': {'predicate': 'created_u_p_sys', 'type': 'current'},
                             'to': {'predicate': 'in_p_sys', 'type': 'always'}},
              }

# The condition is some necessary part of finishing one goal
conditions = {'known_a': ['allocate_s'],
              'in_me_sys': ['reported_s'],
              'invited_a_p': ['allocate_s']}

# The companion is some predicate that will be true until the goal finishes
companions = {'in_me_sys': ['reported_s']}


def display_goal_state():
    for goal in goal_set:
        print("------------------------------------------------------")
        print("Goal ID: ", goal['goal_id'], ", Name: ", goal['name'])
        print("------------------------------------------------------")
        display_state(goal['state'], 1)
        print("------------------------------------------------------")
        print()


# Parse the predicate string to (signed, predicate, objects) dictionary
# which make the comparison easier
def parse_predicate(predicate):
    elements = predicate.split("_")
    signed = True
    obj_start = 1
    # When the string contains not, it means that this is a negative statement
    # of another statement
    if elements[0] == "not":
        signed = False
        predi = elements[1]
        obj_start = 2
    else:
        predi = elements[0]

    return {"signed": signed, "predicate": predi, "objects": elements[obj_start:]}


# Use recursive method to access the goal and
# display their predicate composition of every state
def display_state(states, level):
    for state_id in range(len(states)):
        state = states[state_id]
        for i in range(level):
            print("\t", end="")
        print("[ State ", state_id + 1, "]")
        for key in state.keys():
            predicate_arr = state[key]
            if len(predicate_arr) == 0:
                continue
            for i in range(level):
                print("\t", end="")
            print(key, ":", end=" ")
            for predicate in predicate_arr:
                if isinstance(predicate, str):
                    pred_eles = parse_predicate(predicate)
                    if not pred_eles["signed"]:
                        print("not", end=" ")
                    print(pred_eles["predicate"], end="")
                    print("<", end="")
                    for obj in pred_eles['objects']:
                        print(obj, end=", ")
                    print(">", end="; ")
                else:
                    print()
                    # The entry contains hierarchy state, recursively process it
                    display_state(predicate['state'], level + 1)
            print()


# This function is core function of refinement search
# it will compare every pair of goals and calculate their score
# The score is the possibility that this two goals has hierarchy relationship
def refinement_searching():
    score_dict = dict()
    for idx1 in range(len(goal_set)):
        goal_1 = goal_set[idx1]
        sub_score_dict = dict()
        print("------------------------------------")
        for idx2 in range(len(goal_set)):
            # The same goal don't need to compare with itself.
            if idx1 == idx2:
                continue
            goal_2 = goal_set[idx2]
            print("------------------------------------")
            print(goal_1['goal_id'], ": ", goal_1['name'], " vs ", goal_2['goal_id'], ": ", goal_2['name'])
            # Call the function to get the score between these two goal
            _, _, score = get_subgoal_score(goal_1, goal_2)
            sub_score_dict[goal_2['goal_id']] = score
            print("------------------------------------")
        score_dict[goal_1['goal_id']] = sub_score_dict
        print("------------------------------------")

    return score_dict


# The function to display the result
# Every goal will have their rank of the score with other goal
# Higher the score, more possible the goals have hierarchy relationship
def display_score_info(score_dict):
    for sub_score_item in score_dict.items():
        goal_id = sub_score_item[0]
        # Sort the score with desc order, the higher the score will be in the front
        sorted_sub_arr = sorted(sub_score_item[1].items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
        print("--------------------------------")
        print("Goal Id: ", goal_id, "; Name: ", goal_set[goal_id - 1]['name'])
        print("Hierarchy Score: ")
        for other_goal in sorted_sub_arr:
            # Only display the goal with score higher than 0
            if other_goal[1] > 0:
                rhs_goal_id = other_goal[0]
                print("\t Id: ", rhs_goal_id, "; Name:", goal_set[rhs_goal_id - 1]['name'])
                print("\t Score: ", other_goal[1])
                print()

        print("--------------------------------")

    # print(score_dict)


# Compare the goal pair and get its score
# this function can also be used in hierarchy state compare
def get_subgoal_score(g1, g2):
    max_score = -1
    rst_score = 0
    rst_total = 0
    for g2_substate in g2['state']:
        # For every state in potential super goal, when it come true, the goal come true.
        # so we can select the maximum possibility that make one of the state of potential super goal true.
        total_score = 0
        total_predicate = 0
        # Compare all sub goal state, their cummulative score is the total score of this "sub-goal"
        for g1_substate in g1['state']:
            # for every state pair, get its score
            score, total = get_score_state_with_state(g1_substate, g2_substate)
            total_score += score
            total_predicate += total

        # Empty state or Contradict state
        if total_predicate <= 0:
            continue

        # Calculate the hierarchy possibility
        overall_possibility = total_score / total_predicate

        # Retain the highest score
        if overall_possibility > max_score:
            max_score = overall_possibility
            rst_score = total_score
            rst_total = total_predicate

    return rst_score, rst_total, max_score


def get_score_state_with_state(state1, state2):
    temporals = ['current', 'next', 'always', 'eventually', 'untilbefore', 'untilafter']
    curr_score = 0
    total_entry = 0
    # Compare in every temporal operator
    for temporal in temporals:
        # Compare every predicate in one temporal
        for predicate in state1[temporal]:
            # If the current predicate is not a string, it is a hierarchy state,
            # we should recursively access it
            if not isinstance(predicate, str):
                if len(state2[temporal]) > 0 and not isinstance(state2[temporal][0], str):
                    # Both entry can be recursive accessed
                    rst_score, rst_total, _ = get_subgoal_score(predicate, state2[temporal][0])
                else:
                    # Only current goal can be recursive accessed
                    rst_score, rst_total = is_recur_predicate_contribute(predicate, temporal, state2)
                print("After hierarchy, score: ", rst_score, "; total: ", rst_total)
                curr_score += rst_score
                total_entry += rst_total
                continue
            print("\tCheck [", predicate, "]")
            total_entry += 1
            # Check whether the predicate contribute to the hierarchy score
            contr_rst = is_predicate_contribute(predicate, temporal, state2)
            if contr_rst == 1:
                print("Has same predicate! - ", predicate)
                curr_score += 1
                continue
            if contr_rst == -1:
                # The predicate is contradict with another goal's state
                return 0, 0
            # Check whether the predicate is a milestone to complete a goal
            mile_rst = is_predicate_milestone(predicate, temporal, state2)
            if mile_rst == 1:
                print("Has Milestone! - ", predicate)
                curr_score += 1
                continue
            # Check whether the predicate is a condition to complete a goal
            condi_rst = is_predicate_condition(predicate, temporal, state2)
            if condi_rst == 1:
                print("Has Condition! - ", predicate)
                curr_score += 1
                continue

            # Check whether the predicate is a companion to complete a goal
            if temporal in ('untilbefore', 'untilafter'):
                compa_rst = is_predicate_companion(predicate, temporal, state2)
                if compa_rst == 1:
                    print("Has Companion! - ", predicate)
                    curr_score += 1

    print("curr_score: ", curr_score, "; total_entry: ", total_entry)
    print("\tPossibility: ", curr_score / total_entry)
    print()

    return curr_score, total_entry


# This function is used to check whether the predicate
# is companion to complete a goal
def is_predicate_companion(predicate, key, other_g):
    if key == 'untilafter':
        # Whether the Until After is another goal's eventually
        for other_predicate in other_g['eventually']:
            if isinstance(other_predicate, str):
                if predicate == other_predicate:
                    return 1
    elif key == 'untilbefore':
        # Whether the Until Before is a companion to another goal
        if predicate not in companions.keys():
            return 0
        target_goals = companions[predicate]
        for target in target_goals:
            for other_predicate in other_g['eventually']:
                if isinstance(other_predicate, str):
                    if target == other_predicate:
                        return 1
    return 0


# This function is to check a hierarchy entry with other goal
# the hierarchy's "current" entry compare with other goal's original entry
# where the hierarchy comes from. For example, the hierarchy entry comes from
# eventually, the algorithm will compare the hierarchy entry's current entry
# with another goal's eventually entry
def is_recur_predicate_contribute(hierarchy_entry, key, other_g):
    target_entrys = hierarchy_entry['state']
    score = 0
    total = 0
    for state_entry in target_entrys:
        total += get_total_predicate(state_entry)
        current_entry = state_entry['current']
        for predicate in current_entry:
            if isinstance(predicate, str):
                print("Hierarchy Check: ", predicate)
                # Check whether the hierarchy entry contribute to
                # hierarchy score
                rst = is_predicate_contribute(predicate, key, other_g)
                if rst == 1:
                    score += 1
                    continue
                if rst == -1:
                    # Contradict
                    return 0, 0

    return score, total


# Traverse all the temporal operators to see how many predicate
# that one state of goal has
def get_total_predicate(one_hierarchy_entry):
    temporals = ['current', 'next', 'always', 'eventually', 'untilbefore', 'untilafter']
    total = 0
    for temporal in temporals:
        predi_set = one_hierarchy_entry[temporal]
        for predicate in predi_set:
            # Only consider the string, it is a predicate
            if isinstance(predicate, str):
                total += 1

    return total


# This function is to check whether the predicate
# contribute to hierarchy score with another goal
def is_predicate_contribute(predicate, key, other_g):

    # parse the predicate string to a dict that can describe a predicate
    pred_dict = parse_predicate(predicate)

    for other_predicate in other_g[key]:
        if isinstance(other_predicate, str):
            # Current sentence is atomic sentence
            # Check Conjunction Decomposition
            other_pred_dict = parse_predicate(other_predicate)
            rst = compare_predicate(pred_dict, other_pred_dict)
            if rst != 0:
                return rst

        else:
            # Current sentence is not atomic, we should recursively access it
            state_arr = other_predicate['state']
            for state in state_arr:
                rst = is_predicate_contribute(predicate, 'current', state)
                if rst == -1:
                    return -1
                if rst == 1:
                    return 1

    return 0


# This function is to check whether the predicate is
# a milestone to complete a goal. The milestone set should
# be defined first
def is_predicate_milestone(predicate, key, other_g):
    if predicate not in milestones.keys():
        return 0
    from_case = milestones[predicate]["from"]
    to_case = milestones[predicate]["to"]

    if key == "current":
        possi_type = from_case['type']
        target_predicate = from_case['predicate']
    else:
        possi_type = to_case['type']
        target_predicate = to_case['predicate']

    if possi_type != key:
        candi_keys = [key, possi_type]
    else:
        candi_keys = [key]

    for cand_key in candi_keys:
        for other_predicate in other_g[cand_key]:
            if isinstance(other_predicate, str):
                if other_predicate == target_predicate:
                    return 1
            else:
                state_arr = other_predicate['state']
                for state in state_arr:
                    for inner_cand_key in candi_keys:
                        rst = is_predicate_milestone(predicate, inner_cand_key, state)
                        if rst == 1:
                            return 1

    return 0


# This function is to check whether the predicate is a condition to complete a goal
# the condition set should be defined before
def is_predicate_condition(predicate, key, other_g):
    if predicate not in conditions.keys():
        return 0
    target_predicates = conditions[predicate]
    for target in target_predicates:
        # print(target)
        if key == 'current':
            # Check all other state, to see whether some statements needs this condition
            other_states = ['next', 'always', 'eventually']
            for other_state in other_states:
                for other_predicate in other_g[other_state]:
                    # print('\t', other_predicate)
                    if isinstance(other_predicate, str):
                        if other_predicate == target:
                            return 1
                    else:
                        rst = search_target_in_hierarchy(target, other_predicate['state'])
                        if rst == 1:
                            return 1
        else:
            # Check the entry in the same entry of another goal
            for other_predicate in other_g[key]:
                # print('\t', other_predicate)
                if isinstance(other_predicate, str):
                    if other_predicate == target:
                        return 1
                else:
                    rst = search_target_in_hierarchy(target, other_predicate['state'])
                    if rst == 1:
                        return 1
    return 0


def search_target_in_hierarchy(target, hierarchy_state):
    for sub_hie_state in hierarchy_state:
        sub_curr_state = sub_hie_state['current']
        for curr_predicate in sub_curr_state:
            if isinstance(curr_predicate, str):
                if target == curr_predicate:
                    return 1

    return 0


# 0: not the same, 1: same, -1: contradict
def compare_predicate(pre_dict1, pre_dict2):
    if pre_dict1['predicate'] != pre_dict2['predicate']:
        return 0

    obj_list_1 = pre_dict1['objects']
    obj_list_2 = pre_dict2['objects']

    if len(obj_list_1) != len(obj_list_2):
        return 0

    for idx in range(len(obj_list_1)):
        if obj_list_1[idx] != obj_list_2[idx]:
            return 0

    if pre_dict1['signed'] != pre_dict2['signed']:
        return -1

    return 1


if __name__ == "__main__":
    # display_goal_state()
    score_dict = refinement_searching()
    display_score_info(score_dict)







